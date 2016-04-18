import unittest
from python_ds_algorithms.DataStructures.Trees.ParseTreeExample import ParseTree


class TestParseTree(unittest.TestCase):

    def evaluate(self, expression, result):
        parser = ParseTree()
        parseTree = parser.buildParseTree(expression)
        self.assertEqual(parser.evaluate(parseTree), result)
        print(parseTree)

    def testParseTree(self):
        self.evaluate("( ( 5 + ( 2 * ( 100 / 2 ) ) ) - 5 )", 100)
        self.evaluate("( 10 + 5 )", 15)
        self.evaluate("( 10 / 2 )", 5)
        self.evaluate("( 5 * ( 5 * ( 5 * 5 ) ) ) )", 625)
        self.evaluate("( 10 / ( 5 + ( 3 + 2 ) ) )", 1)
        self.evaluate("( 1 + ( 10 - ( 5 + ( 3 + 2 ) ) ) )", 1)