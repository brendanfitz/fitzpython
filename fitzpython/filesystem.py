import datetime as dt
from os.path import splitext

def add_ts_to_filename(filepath):
    filename, extension = splitext(filepath)
    ts = dt.datetime.today().strftime('%Y%m%dT%H%M%S')
    filename_with_ts = f"{filename}_{ts}{extension}"
    return filename_with_ts


if __name__ == '__main__':
    print(add_ts_to_filename(__file__))