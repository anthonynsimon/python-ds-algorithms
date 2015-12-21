import unittest
from DataStructures.Trees import AVLTree


class TestAVLTree(unittest.TestCase):

    def testAVL(self):
        avlTree = AVLTree.AVLTree()
        avlTree.put(5, 2)
        avlTree.put(6, 3)
        avlTree.put(50, 7)
        avlTree.put(7, 4)
        avlTree.put(1, 1)
        avlTree.put(15, 6)
        avlTree.put(11, 5)
        avlTree[0] = 0

        self.assertEqual(avlTree.get(150), None)
        self.assertEqual(avlTree[0], 0)
        self.assertEqual(avlTree[5], 2)
        self.assertEqual(len(avlTree), 8)
        self.assertEqual(str(avlTree.getMin()), "'0' : 0")
        self.assertEqual(str(avlTree.getMax()), "'50' : 7")


        avlTree.put(60, 10)
        avlTree.put(70, 12)
        avlTree.put(65, 11)
        avlTree.put(55, 8)
        avlTree.put(57, 9)
        avlTree.put(59, 9)
        avlTree.put(-1, 9)
        avlTree[50] = 768

        self.assertEqual(avlTree[50], 768)
        #avlTree.remove(50)
        del avlTree[50]
        self.assertEqual(avlTree[50], None)

        # for node in avlTree:
        #     print(node)

        for i in range(100):
            avlTree.put(i,None)

        # avlTree.visualizeVertical()

        # print(avlTree)


suite = unittest.TestLoader().loadTestsFromTestCase(TestAVLTree)
unittest.TextTestRunner(verbosity=2).run(suite)