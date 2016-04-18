import unittest
from python_ds_algorithms.Misc import BalancedParenthesesChecker


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