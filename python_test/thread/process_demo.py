from multiprocessing import Process
import os
import time
"""
  multiprocessing 多线程
"""


def work(identifier):
    print('hey, i am a process{}, pid:{}'.format(identifier, os.getpid()))


def main():
    processes = [
        Process(target=work, args=(number, ))
        for number in range(5)
    ]

    for process in processes:
        process.start()

    while processes:
        processes.pop().join()


if __name__ == '__main__':
    started = time.time()
    main()
    elapsed = time.time() - started
    print('elapsed--{}'.format(elapsed))