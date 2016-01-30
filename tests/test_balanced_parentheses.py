import unittest
from lib.playground.balanced_parentheses_checker import ParenthesesChecker


class TestBalancedParentheses(unittest.TestCase):

    def testForFalse(self):
        checker = ParenthesesChecker()
        self.assertFalse(checker.check("("))
        self.assertFalse(checker.check(")"))
        self.assertFalse(checker.check("(()"))
        self.assertFalse(checker.check(")))(((()()"))

    def testForTrue(self):
        checker = ParenthesesChecker()
        self.assertTrue(checker.check(""))
        self.assertTrue(checker.check("()"))
        self.assertTrue(checker.check("(((())))()(())(()())"))
        self.assertTrue(checker.check("()()()(())(()()(()))"))