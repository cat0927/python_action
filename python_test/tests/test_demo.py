import unittest
from python_test.big_data.cache_demo import _sum
"""
 单元测试
"""


class MyTests(unittest.TestCase):
    def test_sum(self):
        self.assertIsNotNone(_sum(2, 3))


if __name__ == '__main__':
    unittest.main()
