import timeit
from _collections import deque
"""
  deque 类型
"""


# List 类型
def seq():
    sequence = list(range(10))
    sequence.append(0)
    sequence.pop()


# deque 类型
def deque_seq():
    sequence_deq = deque(range(10))
    sequence_deq.append(0)
    sequence_deq.pop()


def seq_insert():
    sequence = list(range(10))
    sequence.insert(0, 0)
    sequence.pop(0)


def deq_append():
    sequence_deq = deque(range(10))
    sequence_deq.appendleft(0)
    sequence_deq.popleft()


if __name__ == '__main__':
    print(timeit.timeit(seq, number=1000000))
    print(timeit.timeit(deque_seq, number=1000000))
    print('--------')
    print(timeit.timeit(seq_insert, number=1000000))
    print(timeit.timeit(deq_append, number=1000000))