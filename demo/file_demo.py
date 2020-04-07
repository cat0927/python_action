"""
 file 读、写
"""

def read_file():
    try:
        file = open("file.txt")
        print("read_file:{}".format(file.readlines()))
    except Exception as ex:
        print("Exception:{}".format(ex))
    finally:
        file.close()


def write_file():
    try:
        file = open("file.txt", "a", encoding="utf-8")
        file.writelines(["\n 张三","李四"])
    except Exception as ex:
        print("Exception:{}".format(ex))
    finally:
        file.close()


if __name__ == '__main__':
    print("-------")
    read_file()
    write_file()
    read_file()