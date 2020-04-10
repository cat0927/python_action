import pathlib
import datetime

"""
  归档到固定时间目录下
"""


file_path = "*.txt"
archive = "archive"


if __name__ == '__main__':
    print('-----------')

    date_str = datetime.date.today().strftime("%Y-%m-%d")
    cur_path = pathlib.Path(".")
    new_path = cur_path.joinpath(archive, date_str)
    new_path.mkdir()

    paths = cur_path.glob(file_path)

    for path in paths:
        path.rename(new_path.joinpath(path.name))