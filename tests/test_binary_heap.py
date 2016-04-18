import unittest
from DataStructures.Trees.BinaryHeap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def testBinaryHeap(self):
        binaryHeap = BinaryHeap()
        self.assertTrue(binaryHeap.isEmpty())

        binaryHeap.insert(1)
        binaryHeap.insert(4)
        binaryHeap.insert(5)
        binaryHeap.insert(3)
        binaryHeap.insert(2)
        binaryHeap.insert(6)
        binaryHeap.deleteMin()

        self.assertEqual(binaryHeap.findMin(), 2)
        self.assertEqual(binaryHeap.size(), 5)
        self.assertFalse(binaryHeap.isEmpty())

        binaryHeap.buildHeap([99,77,33,22,55,66,11,44,99])
        self.assertEqual(binaryHeap.findMin(), 11)
        self.assertEqual(binaryHeap.size(), 9)
        self.assertFalse(binaryHeap.isEmpty())