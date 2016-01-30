import unittest
from lib.data_structures.trees.binary_heap import BinaryHeap


class TestBinaryHeap(unittest.TestCase):

    def testBinaryHeap(self):
        heap = BinaryHeap()
        self.assertTrue(heap.is_empty())

        heap.insert(1)
        heap.insert(4)
        heap.insert(5)
        heap.insert(3)
        heap.insert(2)
        heap.insert(6)
        heap.delete_min()

        self.assertEqual(heap.find_min(), 2)
        self.assertEqual(heap.size(), 5)
        self.assertFalse(heap.is_empty())

        heap.build_heap([99, 77, 33, 22, 55, 66, 11, 44, 99])
        self.assertEqual(heap.find_min(), 11)
        self.assertEqual(heap.size(), 9)
        self.assertFalse(heap.is_empty())