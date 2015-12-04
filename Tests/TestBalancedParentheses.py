import unittest
from Misc import BalancedParenthesesChecker

class TestBalancedParentheses(unittest.TestCase):

    def testForFalse(self):
        checker = BalancedParenthesesChecker.ParenthesesChecker()
        self.assertFalse(checker.check("("))
        self.assertFalse(checker.check(")"))
        self.assertFalse(checker.check("(()"))
        self.assertFalse(checker.check(")))(((()()"))

    def testForTrue(self):
        checker = BalancedParenthesesChecker.ParenthesesChecker()
        self.assertTrue(checker.check(""))
        self.assertTrue(checker.check("()"))
        self.assertTrue(checker.check("(((())))()(())(()())"))
        self.assertTrue(checker.check("()()()(())(()()(()))"))

suite = unittest.TestLoader().loadTestsFromTestCase(TestBalancedParentheses)
unittest.TextTestRunner(verbosity=2).run(suite)