import unittest
import random
from lib.data_structures.trees.binary_search_tree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def testBST(self):
        bst = BinarySearchTree()
        bst.put(5, 2)
        bst.put(6, 3)
        bst.put(50, 7)
        bst.put(7, 4)
        bst.put(1, 1)
        bst.put(15, 6)
        bst.put(11, 5)
        bst[0] = 0

        self.assertEqual(bst.get(150), None)
        self.assertEqual(bst[0], 0)
        self.assertEqual(bst[5], 2)
        self.assertEqual(len(bst), 8)
        self.assertEqual(str(bst.get_min()), "'0' : 0")
        self.assertEqual(str(bst.get_max()), "'50' : 7")


        bst.put(60, 10)
        bst.put(70, 12)
        bst.put(65, 11)
        bst.put(55, 8)
        bst.put(57, 9)
        bst[50] = 768

        self.assertEqual(bst[50], 768)
        del bst[50]
        self.assertEqual(bst[50], None)

        for i in range(150):
            bst.put(i, None)

        for i in range(150):
            del bst[random.randrange(0,150)]

        bst.visualize_vertical()

        # print("height", bstTree.root.getSubtreeHeight())