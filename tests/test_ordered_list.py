from DataStructures import OrderedList
import unittest


class TestOrderedList(unittest.TestCase):

    def test(self):
        oList = OrderedList.OrderedList()

        self.assertTrue(oList.isEmpty())

        oList.add(7)
        oList.add(0)
        oList.add(3)

        self.assertFalse(oList.isEmpty())
        self.assertEqual(oList.size(), 3)
        self.assertEqual(str(oList), "[0, 3, 7]")

        oList.add(6)
        oList.remove(3)
        oList.add(2)

        self.assertEqual(str(oList), "[0, 2, 6, 7]")
        self.assertEqual(oList.size(), 4)
        self.assertEqual(oList.pop(), 7)
        self.assertEqual(oList.pop(), 6)
        self.assertEqual(str(oList), "[0, 2]")
        self.assertFalse(oList.isEmpty())

        oList.clear()

        self.assertTrue(oList.isEmpty())
        self.assertEqual(oList.size(), 0)
        self.assertEqual(str(oList), "[]")

        self.assertEqual(oList.pop(), None)

        oList.add(6)

        self.assertEqual(str(oList), "[6]")
        self.assertEqual(oList.remove(3), None)
        self.assertTrue(oList.search(6))
        self.assertFalse(oList.search(77))

        oList.add(2)

        self.assertEqual(str(oList), "[2, 6]")