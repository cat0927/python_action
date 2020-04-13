import time
import datetime


def test_ime():
    ts = time.time()
    print("ts", ts)
    date_time = time.localtime(ts)
    print("date_time", date_time)


def test_date_time():
    current_time = datetime.datetime.now()
    print("current_time: {}".format(current_time))
    print("year:{}".format(current_time.year))
    print("month:{}".format(current_time.month))
    print("day:{}".format(current_time.day))

    time.sleep(1)

    end_time = datetime.datetime.now()
    print("run_time:{} 秒".format(end_time.second - current_time.second))

    format_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("format_time:{}".format(format_time))

    # 默认格式
    format_date_time = datetime.datetime.fromtimestamp(time.time())
    print("format_date_time:{}".format(format_date_time))


if __name__ == '__main__':
    print("---------")
    test_ime()
    test_date_time()