from matplotlib.ticker import FuncFormatter

def millions(x, pos):
    """
    The two args are the value and tick position
    """
    return '$%1.0fM' % (x*1e-6)
MIL_FORMATTER = FuncFormatter(millions)

def percent(x, pos):
    return '{:,.2%}'.format(x)
PERCENT_FORMATTER = FuncFormatter(percent)

def rotate_xticklabels(ax, rot):
    for item in ax.get_xticklabels():
        item.set_rotation(rot)