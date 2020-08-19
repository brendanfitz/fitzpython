# pandas_utils.py

def format_cols(colname, direction='in'):
    if direction == 'in':
        return (colname
            .lower()
            .replace(' ', '_')
            .replace('(', '')
            .replace(')', '')
        )
    elif direction == 'out':
        return (colname.replace('_', ' ')
            .title()
        )
    raise ValueError('Direction must be "in" or "out"')