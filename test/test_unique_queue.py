from src.UniqueQueue import *
import unittest


class Foo:
    def __init__(self, index, data):
        self.index = index
        self.data = data

    def same_element(self, other):
        if self.index == other.index:
            return True
        else:
            return False


class TestUniqueQueue(unittest.TestCase):
    def setUp(self):
        self.queue = UniqueQueue()

    def test_append(self):
        self.queue.append(Foo(1, 10))
        self.queue.append(Foo(2, 20))
        self.queue.append(Foo(1, 30))
        self.queue.append(Foo(3, 40))
        self.assertEqual(len(self.queue), 3)


if __name__ == '__main__':
    unittest.main()
