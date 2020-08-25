# pandas_utils.py

def format_cols(colname, direction='in'):
    """Formats columns beween human-readable and pandorable

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
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