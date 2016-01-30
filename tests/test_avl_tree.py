import unittest
import random
from lib.data_structures.trees.avl_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def testAVL(self):
        avl_tree = AVLTree()
        avl_tree.put(5, 2)
        avl_tree.put(6, 3)
        avl_tree.put(50, 7)
        avl_tree.put(7, 4)
        avl_tree.put(1, 1)
        avl_tree.put(15, 6)
        avl_tree.put(11, 5)
        avl_tree[0] = 0

        self.assertEqual(avl_tree.get(150), None)
        self.assertEqual(avl_tree[0], 0)
        self.assertEqual(avl_tree[5], 2)
        self.assertEqual(len(avl_tree), 8)
        self.assertEqual(str(avl_tree.get_min()), "'0' : 0")
        self.assertEqual(str(avl_tree.get_max()), "'50' : 7")


        avl_tree.put(60, 10)
        avl_tree.put(70, 12)
        avl_tree.put(65, 11)
        avl_tree.put(55, 8)
        avl_tree.put(57, 9)
        avl_tree.put(59, 9)
        avl_tree.put(-1, 9)
        avl_tree[50] = 768

        self.assertEqual(avl_tree[50], 768)
        # avlTree.remove(50)
        del avl_tree[50]
        self.assertEqual(avl_tree[50], None)

        for i in range(150):
            avl_tree.put(i,None)

        for i in range(150):
            del avl_tree[random.randrange(0,150)]

        avl_tree.visualize_vertical()

        print("height", avl_tree.root.get_subtree_height())
        print("balance", avl_tree.root.get_balance_factor())
