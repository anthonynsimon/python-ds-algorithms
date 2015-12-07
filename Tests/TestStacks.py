import unittest
from DataStructures import Stacks

class TestStacks(unittest.TestCase):

    def testLLStack(self):
        stack = Stacks.StackLL()

        self.assertIsNone(stack.peek())
        self.assertEqual(stack.size(),0)
        self.assertTrue(stack.isEmpty())

        stack.push("Marcus")
        stack.push(5)
        stack.push(False)
        stack.push(67.128)
        stack.push("Carlos")
        stack.push(Stacks.StackLLNode)
        stack.push(8)

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.size(), 7)

        stack.pop()
        stack.pop()
        stack.pop()

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), 67.128)
        self.assertEqual(stack.size(), 4)

        self.assertEqual(str(stack), "['Marcus', 5, False, 67.128]")

        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

        self.assertIsNone(stack.peek())
        self.assertEqual(stack.size(),0)
        self.assertTrue(stack.isEmpty())


    def testALStack(self):
        stack = Stacks.StackAA()

        self.assertIsNone(stack.peek())
        self.assertEqual(stack.size(),0)
        self.assertTrue(stack.isEmpty())

        stack.push("Marcus")
        stack.push(5)
        stack.push(False)
        stack.push(67.128)
        stack.push("Carlos")
        stack.push(Stacks.StackLLNode)
        stack.push(8)

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.size(), 7)

        stack.pop()
        stack.pop()
        stack.pop()

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), 67.128)
        self.assertEqual(stack.size(), 4)

        self.assertEqual(str(stack), "['Marcus', 5, False, 67.128]")

        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

        self.assertIsNone(stack.peek())
        self.assertEqual(stack.size(),0)
        self.assertTrue(stack.isEmpty())

    def testALIStack(self):
        stack = Stacks.StackAI()

        self.assertIsNone(stack.peek())
        self.assertEqual(stack.size(),0)
        self.assertTrue(stack.isEmpty())

        stack.push("Marcus")
        stack.push(5)
        stack.push(False)
        stack.push(67.128)
        stack.push("Carlos")
        stack.push(Stacks.StackLLNode)
        stack.push(8)

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.size(), 7)

        stack.pop()
        stack.pop()
        stack.pop()

        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.peek(), 67.128)
        self.assertEqual(stack.size(), 4)

        self.assertEqual(str(stack), "['Marcus', 5, False, 67.128]")

        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

        self.assertIsNone(stack.peek())
        self.assertEqual(stack.size(),0)
        self.assertTrue(stack.isEmpty())

suite = unittest.TestLoader().loadTestsFromTestCase(TestStacks)
unittest.TextTestRunner(verbosity=2).run(suite)
