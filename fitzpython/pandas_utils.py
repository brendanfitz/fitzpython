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
    
    
from openpyxl.utils import get_column_letter

def autofit_column_widths(ws):
    for col in ws.columns:
         max_length = 0
         column = col[0].column
         for cell in col:
             try: # Necessary to avoid error on empty cells
                 if len(str(cell.value)) > max_length:
                     max_length = len(cell.value)
             except:
                 pass
         adjusted_width = (max_length + 2) * 1.2
         ws.column_dimensions[get_column_letter(column)].width = adjusted_width
