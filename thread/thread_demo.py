from threading import Thread
import time
import os
"""
  多线程，每执行一个任务，创建一个线程
"""


PLACES = (
    'Reykjavik', 'Vien', 'Zadar', 'Venice', 'Wroclaw', 'Bolognia', 'Berlin'
    , 'Slubice', 'New York', 'Dehli'
)


# 具体执行逻辑
def fetch_place(place):
    time.sleep(2)
    print('fetch_place:{},pid:{}'.format(place, os.getpid()))


def main():
    threads = []
    for place in PLACES:
        thread = Thread(target=fetch_place, args=[place])
        thread.start()
        threads.append(thread)

    while threads:
        threads.pop().join()


if __name__ == '__main__':
    started = time.time()
    main()
    elapsed = time.time() - started
    print('elapsed--{}'.format(elapsed))