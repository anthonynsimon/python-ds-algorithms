import operator
from lib.data_structures.stack import StackLL
from lib.data_structures.trees.binary_tree import BinaryTree


class ParseTree(object):

    def build_parse_tree(self, expression):
        stack = StackLL()
        root_tree = BinaryTree('')
        current_tree = root_tree
        expression = expression.split()
        for token in expression:
            if token == '(':
                stack.push(current_tree)
                current_tree.insert_left_child(BinaryTree(''))
                current_tree = current_tree.get_left_child()
            elif token == ')':
                current_tree = stack.pop()
            elif token in ['+', '-', '/', '*']:
                current_tree.set_root_key(token)
                stack.push(current_tree)
                current_tree.insert_right_child((BinaryTree('')))
                current_tree = current_tree.get_right_child()
            elif token not in ['+', '-', '/', '*']:
                current_tree.set_root_key(int(token))
                current_tree = stack.pop()
            else:
                raise "INVALID EXPRESSION"
        return root_tree


    # evaluate the tree with a postorder traversal
    def evaluate(self, tree):
        if tree:
            operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}

            left = tree.get_left_child()
            right = tree.get_right_child()

            if left and right:
                fn = operators[tree.get_root_key()]
                return fn(self.evaluate(left), self.evaluate(right))
            else:
                return tree.get_root_key()