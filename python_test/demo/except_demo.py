
def open_file():
    print("准备打开一个文件")
    try:
        file = open("ClassDemo1.py")
        print("file open", file)
    except (FileNotFoundError, FileExistsError) as ex:
        print("FileNotFoundError error", ex)
        # 向上抛异常
        # raise Exception
    except Exception as ex:
        print("Exception", ex)
    finally:
        print("finally.....")


def open_file1():
    open_file()


if __name__ == '__main__':
    print("---------")
    open_file1()
