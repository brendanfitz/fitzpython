"""
Created on Thu Nov 30 06:28:00 2020
"""

import statsmodels.api as sm
import itertools

class BackwardsSelector(object):
    
    def __init__(self, df, endog_varname, criterion, alpha=None):
        self.df = df        
        self.Y = df.loc[:, endog_varname]
        
        self.criterion = criterion
        self.alpha = alpha
        
        columns = df.columns.tolist()
        self.exog_varnames = [x for x in columns if x != endog_varname]
        self.dropped_exog_varnames = list()
    
    def backwards_select(self):
        if self.criterion == 'pvalue':
            step = self.step_pvalue
        elif self.criterion == 'rsquared_adj':
            step = self.step_rsquared_adj
        
        results, exog_varname_to_drop = step()
        
        while exog_varname_to_drop is not None:
            results, exog_varname_to_drop = step()
        
        return results, self.exog_varnames
    
    def step_pvalue(self, verbose=1):
        X = sm.tools.tools.add_constant(self.df.loc[:, self.exog_varnames])
        model = sm.OLS(self.Y, X)
        results = model.fit()
        
        exog_varname_to_drop = (results
            .pvalues
            .drop('const')
            .nlargest(1)
            .index[0]
        )
        
        if results.pvalues.nlargest(1)[0] <= self.alpha:
            return results, None
        
        if verbose > 1:
            print(results.summary())
        elif verbose == 1:
            print(f'Dropping {exog_varname_to_drop}')
        
        self.dropped_exog_varnames.append(exog_varname_to_drop)
        self.exog_varnames.remove(exog_varname_to_drop)
        
        return results, exog_varname_to_drop
    
    def step_rsquared_adj(self):
        exog_varnames_combos = list(itertools.combinations(self.exog_varnames , len(self.exog_varnames)-1)) + [set(self.exog_varnames)]
        results_set = list()
        for exog_varnames in exog_varnames_combos:
            X = sm.tools.tools.add_constant(self.df.loc[:, exog_varnames])
            model = sm.OLS(self.Y, X)
            results = model.fit()
            results_set.append(results)
            
        model_results_with_highest_rsquared = max(results_set, key=lambda x: x.rsquared_adj)
        
        column_to_drop = set(exog_varnames) - set(model_results_with_highest_rsquared .model.exog_names)
        
        if len(column_to_drop) == 0:
            return model_results_with_highest_rsquared, None
            
        exog_varname_to_drop = column_to_drop.pop()
        
        self.dropped_exog_varnames.append(exog_varname_to_drop)
        self.exog_varnames.remove(exog_varname_to_drop)

        return model_results_with_highest_rsquared, exog_varname_to_drop
