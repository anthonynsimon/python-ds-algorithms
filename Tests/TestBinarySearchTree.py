import unittest
from DataStructures.Trees import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def testBST(self):
        bstTree = BinarySearchTree.BinarySearchTree()
        bstTree.put(5, 2)
        bstTree.put(6, 3)
        bstTree.put(50, 7)
        bstTree.put(7, 4)
        bstTree.put(1, 1)
        bstTree.put(15, 6)
        bstTree.put(11, 5)
        bstTree[0] = 0

        self.assertEqual(bstTree.get(150), None)
        self.assertEqual(bstTree[0], 0)
        self.assertEqual(bstTree[5], 2)
        self.assertEqual(len(bstTree), 8)
        self.assertEqual(str(bstTree.getMin()), "'0' : 0")
        self.assertEqual(str(bstTree.getMax()), "'50' : 7")


        bstTree.put(60, 10)
        bstTree.put(70, 12)
        bstTree.put(65, 11)
        bstTree.put(55, 8)
        bstTree.put(57, 9)
        bstTree[50] = 768

        self.assertEqual(bstTree[50], 768)
        bstTree.remove(50)
        #del bstTree[50]
        self.assertEqual(bstTree[50], None)

        for node in bstTree:
            print(node)

        bstTree.visualize()

        print(bstTree)


suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearchTree)
unittest.TextTestRunner(verbosity=2).run(suite)