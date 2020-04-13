import asyncio
import os
from threading import Thread

"""
 异步调用
"""


async def print_number(number):
    print("number:{}, pid:{}, thread_name:{}".format(number, os.getpid(), Thread.getName))


if __name__ == '__main__':
    print('-------------')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.wait([
            print_number(number)
            for number in range(10)
        ])
    )
