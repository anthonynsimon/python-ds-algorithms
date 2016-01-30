import unittest
from lib.data_structures.queue import QueueLL, QueueAA


class TestQueue(unittest.TestCase):

    def testALQueueTest(self):
        queue = QueueAA()
        self.assertEqual(queue.size(),0)
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("First")
        queue.enqueue(2)
        queue.enqueue("Third")

        self.assertEqual(queue.size(),3)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), "First")
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), "Third")
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("Fourth")
        self.assertEqual(queue.dequeue(), "Fourth")
        queue.enqueue("Uno")
        queue.enqueue("Dos")
        queue.clear()
        self.assertEqual(queue.is_empty(), True)

    def testLLQueueTest(self):
        queue = QueueLL()
        self.assertEqual(queue.size(),0)
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("First")
        queue.enqueue(2)
        queue.enqueue("Third")

        self.assertEqual(queue.size(),3)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.dequeue(), "First")
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), "Third")
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("Fourth")
        self.assertEqual(queue.dequeue(), "Fourth")
        queue.enqueue("Uno")
        queue.enqueue("Dos")
        queue.clear()
        self.assertEqual(queue.is_empty(), True)