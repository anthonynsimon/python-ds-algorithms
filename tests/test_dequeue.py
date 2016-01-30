import unittest
from lib.data_structures.deque import Deque


class TestDeque(unittest.TestCase):

    def testALDeque(self):
        deque = Deque()
        self.assertTrue(deque.is_empty())

        deque.add_tail("Third")
        deque.add_head("Second")
        deque.add_head("First")

        self.assertFalse(deque.is_empty())
        self.assertEqual(deque.remote_tail(), "Third")
        self.assertEqual(deque.remote_tail(), "Second")
        self.assertEqual(deque.remove_head(), "First")
        self.assertEqual(deque.remote_tail(), None)
        self.assertEqual(deque.remove_head(), None)

        deque.add_tail("Third")
        deque.add_head("Second")
        deque.add_head("First")

        self.assertEqual(deque.size(), 3)
        deque.clear()
        self.assertEqual(deque.size(), 0)