import unittest
from python_ds_algorithms.DataStructures import Queue


class TestQueue(unittest.TestCase):

    def testALQueueTest(self):
        queue = Queue.QueueAA()
        self.assertEqual(queue.size(),0)
        self.assertTrue(queue.isEmpty())
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("First")
        queue.enqueue(2)
        queue.enqueue("Third")

        self.assertEqual(queue.size(),3)
        self.assertFalse(queue.isEmpty())
        self.assertEqual(queue.dequeue(), "First")
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), "Third")
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("Fourth")
        self.assertEqual(queue.dequeue(), "Fourth")
        queue.enqueue("Uno")
        queue.enqueue("Dos")
        queue.clear()
        self.assertEqual(queue.isEmpty(), True)

    def testLLQueueTest(self):
        queue = Queue.QueueLL()
        self.assertEqual(queue.size(),0)
        self.assertTrue(queue.isEmpty())
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("First")
        queue.enqueue(2)
        queue.enqueue("Third")

        self.assertEqual(queue.size(),3)
        self.assertFalse(queue.isEmpty())
        self.assertEqual(queue.dequeue(), "First")
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), "Third")
        self.assertEqual(queue.dequeue(), None)

        queue.enqueue("Fourth")
        self.assertEqual(queue.dequeue(), "Fourth")
        queue.enqueue("Uno")
        queue.enqueue("Dos")
        queue.clear()
        self.assertEqual(queue.isEmpty(), True)