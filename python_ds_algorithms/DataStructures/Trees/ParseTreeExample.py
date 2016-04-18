import operator
from python_ds_algorithms.DataStructures.Stacks import StackLL
from python_ds_algorithms.DataStructures.Trees.BinaryTree import BinaryTree


class ParseTree(object):

    def buildParseTree(self, expression):
        stack = StackLL()
        rootTree = BinaryTree('')
        currentTree = rootTree
        expression = expression.split()
        for token in expression:
            if token == '(':
                stack.push(currentTree)
                currentTree.insertLeftChild(BinaryTree(''))
                currentTree = currentTree.getLeftChild()
            elif token == ')':
                currentTree = stack.pop()
            elif token in ['+', '-', '/', '*']:
                currentTree.setRootKey(token)
                stack.push(currentTree)
                currentTree.insertRightChild((BinaryTree('')))
                currentTree = currentTree.getRightChild()
            elif token not in ['+', '-', '/', '*']:
                currentTree.setRootKey(int(token))
                currentTree = stack.pop()
            else:
                raise "INVALID EXPRESSION"
        return rootTree


    # evaluate the tree with a postorder traversal
    def evaluate(self, tree):
        if tree:
            operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}

            leftChild = tree.getLeftChild()
            rightChild = tree.getRightChild()

            if leftChild and rightChild:
                fn = operators[tree.getRootKey()]
                return fn(self.evaluate(leftChild), self.evaluate(rightChild))
            else:
                return tree.getRootKey()