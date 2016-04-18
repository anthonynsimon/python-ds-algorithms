import unittest
from python_ds_algorithms.DataStructures import Deque


class TestDeque(unittest.TestCase):

    def testALDeque(self):
        deque = Deque.Deque()
        self.assertTrue(deque.isEmpty())

        deque.addTail("Third")
        deque.addHead("Second")
        deque.addHead("First")

        self.assertFalse(deque.isEmpty())
        self.assertEqual(deque.removeTail(), "Third")
        self.assertEqual(deque.removeTail(), "Second")
        self.assertEqual(deque.removeHead(), "First")
        self.assertEqual(deque.removeTail(), None)
        self.assertEqual(deque.removeHead(), None)

        deque.addTail("Third")
        deque.addHead("Second")
        deque.addHead("First")

        self.assertEqual(deque.size(), 3)
        deque.clear()
        self.assertEqual(deque.size(), 0)