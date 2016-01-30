from lib.data_structures.ordered_list import OrderedList
import unittest


class TestOrderedList(unittest.TestCase):

    def test(self):
        ordered_list = OrderedList()

        self.assertTrue(ordered_list.is_empty())

        ordered_list.add(7)
        ordered_list.add(0)
        ordered_list.add(3)

        self.assertFalse(ordered_list.is_empty())
        self.assertEqual(ordered_list.size(), 3)
        self.assertEqual(str(ordered_list), "[0, 3, 7]")

        ordered_list.add(6)
        ordered_list.remove(3)
        ordered_list.add(2)

        self.assertEqual(str(ordered_list), "[0, 2, 6, 7]")
        self.assertEqual(ordered_list.size(), 4)
        self.assertEqual(ordered_list.pop(), 7)
        self.assertEqual(ordered_list.pop(), 6)
        self.assertEqual(str(ordered_list), "[0, 2]")
        self.assertFalse(ordered_list.is_empty())

        ordered_list.clear()

        self.assertTrue(ordered_list.is_empty())
        self.assertEqual(ordered_list.size(), 0)
        self.assertEqual(str(ordered_list), "[]")

        self.assertEqual(ordered_list.pop(), None)

        ordered_list.add(6)

        self.assertEqual(str(ordered_list), "[6]")
        self.assertEqual(ordered_list.remove(3), None)
        self.assertTrue(ordered_list.search(6))
        self.assertFalse(ordered_list.search(77))

        ordered_list.add(2)

        self.assertEqual(str(ordered_list), "[2, 6]")