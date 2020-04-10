"""
  归档文件为带时间戳
"""

import pathlib
import datetime

file_path = "*.txt"
archive = "archive"


if __name__ == '__main__':
    print('-------文件归档-----')
    # 日期生成字符串
    date_str = datetime.date.today().strftime("%Y-%m-%d")

    curr_path = pathlib.Path(".")
    paths = curr_path.glob(file_path)

    for path in paths:
        new_filename = "{}_{}{}".format(path.stem, date_str, path.suffix)
        new_path = curr_path.joinpath(archive, new_filename)
        path.rename(new_path)