from queue import Queue, Empty
from threading import Thread
from thread.thread_demo import fetch_place, PLACES
import time

"""
  线程池
"""

THREAD_POOL_SIZE = 4


def worker(work_queue):
    while not work_queue.empty():
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            fetch_place(item)
            work_queue.task_done()


def main():
    work_queue = Queue()
    for place in PLACES:
        work_queue.put(place)

    threads = [
        Thread(target=worker, args=(work_queue,))
        for _ in range(THREAD_POOL_SIZE)
    ]

    for thread in threads:
        thread.start()

    work_queue.join()

    while threads:
        threads.pop().join()


if __name__ == '__main__':
    started = time.time()
    main()
    elapsed = time.time() - started
    print('elapsed--{}'.format(elapsed))
