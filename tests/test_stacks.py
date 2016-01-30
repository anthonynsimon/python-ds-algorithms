import unittest
from lib.data_structures.stack import StackLL, StackAI, StackAA, StackLLNode


class TestStacks(unittest.TestCase):

    def testLLStack(self):
        stack_ll = StackLL()
        self.assertIsNone(stack_ll.peek())
        self.assertEqual(stack_ll.size(),0)
        self.assertTrue(stack_ll.is_empty())

        stack_ll.push("Marcus")
        stack_ll.push(5)
        stack_ll.push(False)
        stack_ll.push(67.128)
        stack_ll.push("Carlos")
        stack_ll.push(StackLLNode)
        stack_ll.push(8)

        self.assertFalse(stack_ll.is_empty())
        self.assertEqual(stack_ll.peek(), 8)
        self.assertEqual(stack_ll.size(), 7)

        stack_ll.pop()
        stack_ll.pop()
        stack_ll.pop()

        self.assertFalse(stack_ll.is_empty())
        self.assertEqual(stack_ll.peek(), 67.128)
        self.assertEqual(stack_ll.size(), 4)

        self.assertEqual(str(stack_ll), "['Marcus', 5, False, 67.128]")

        stack_ll.pop()
        stack_ll.pop()
        stack_ll.pop()
        stack_ll.pop()
        stack_ll.pop()
        stack_ll.pop()

        self.assertIsNone(stack_ll.peek())
        self.assertEqual(stack_ll.size(),0)
        self.assertTrue(stack_ll.is_empty())

    def testALStack(self):
        stack_aa = StackAA()
        self.assertIsNone(stack_aa.peek())
        self.assertEqual(stack_aa.size(),0)
        self.assertTrue(stack_aa.is_empty())

        stack_aa.push("Marcus")
        stack_aa.push(5)
        stack_aa.push(False)
        stack_aa.push(67.128)
        stack_aa.push("Carlos")
        stack_aa.push(StackLLNode)
        stack_aa.push(8)

        self.assertFalse(stack_aa.is_empty())
        self.assertEqual(stack_aa.peek(), 8)
        self.assertEqual(stack_aa.size(), 7)

        stack_aa.pop()
        stack_aa.pop()
        stack_aa.pop()

        self.assertFalse(stack_aa.is_empty())
        self.assertEqual(stack_aa.peek(), 67.128)
        self.assertEqual(stack_aa.size(), 4)

        self.assertEqual(str(stack_aa), "['Marcus', 5, False, 67.128]")

        stack_aa.pop()
        stack_aa.pop()
        stack_aa.pop()
        stack_aa.pop()
        stack_aa.pop()
        stack_aa.pop()

        self.assertIsNone(stack_aa.peek())
        self.assertEqual(stack_aa.size(),0)
        self.assertTrue(stack_aa.is_empty())

    def testALIStack(self):
        stack_ai = StackAI()
        self.assertIsNone(stack_ai.peek())
        self.assertEqual(stack_ai.size(),0)
        self.assertTrue(stack_ai.is_empty())

        stack_ai.push("Marcus")
        stack_ai.push(5)
        stack_ai.push(False)
        stack_ai.push(67.128)
        stack_ai.push("Carlos")
        stack_ai.push(StackLLNode)
        stack_ai.push(8)

        self.assertFalse(stack_ai.is_empty())
        self.assertEqual(stack_ai.peek(), 8)
        self.assertEqual(stack_ai.size(), 7)

        stack_ai.pop()
        stack_ai.pop()
        stack_ai.pop()

        self.assertFalse(stack_ai.is_empty())
        self.assertEqual(stack_ai.peek(), 67.128)
        self.assertEqual(stack_ai.size(), 4)

        self.assertEqual(str(stack_ai), "['Marcus', 5, False, 67.128]")

        stack_ai.pop()
        stack_ai.pop()
        stack_ai.pop()
        stack_ai.pop()
        stack_ai.pop()
        stack_ai.pop()

        self.assertIsNone(stack_ai.peek())
        self.assertEqual(stack_ai.size(),0)
        self.assertTrue(stack_ai.is_empty())