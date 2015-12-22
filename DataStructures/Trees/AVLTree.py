from DataStructures.Trees import BinarySearchTree

class AVLNode(BinarySearchTree.BSTNode):
    def getBalanceFactor(self):
        leftSide = 0
        rightSide = 0
        if self.hasLeftChild():
            leftSide = self.getLeftChild().getSubtreeHeight() + 1
        if self.hasRightChild():
            rightSide = self.getRightChild().getSubtreeHeight() + 1
        return leftSide - rightSide


class AVLTree(BinarySearchTree.BinarySearchTree):

    def __init__(self):
        super(AVLTree, self).__init__()

    def put(self, key, value):
        if self.root is None:
            self.root = AVLNode(key, value)
            self.count = 1
        else:
            currentNode = self.root
            done = False
            while not done:
                if currentNode.key == key:
                    currentNode.value = value
                    done = True
                elif currentNode.key > key:
                    if currentNode.hasLeftChild():
                        currentNode = currentNode.getLeftChild()
                    else:
                        currentNode.left = AVLNode(key, value, None, None, currentNode)
                        done = True
                elif currentNode.key < key:
                    if currentNode.hasRightChild():
                        currentNode = currentNode.getRightChild()
                    else:
                        currentNode.right = AVLNode(key, value, None, None, currentNode)
                        done = True
            self.count += 1
            self.rebalance(currentNode)

    def remove(self, key):
        currentNode = self.get(key)
        if currentNode:
            rebalancerNode = None

            # If it has no children
            if currentNode.isLeaf():
                if currentNode.isRoot():
                    self.root = None
                else:
                    rebalancerNode = currentNode.getParent()
                    if currentNode == currentNode.parent.getLeftChild():
                        currentNode.getParent().left = None
                    else:
                        currentNode.getParent().right = None

            # If it has both children
            elif currentNode.hasBothChildren():
                successorNode = self.getSuccessor(currentNode)
                rebalancerNode = successorNode.getParent()
                tempKey = successorNode.key
                tempValue = successorNode.value
                self.remove(successorNode.key) # must clear it before changing the BST path
                currentNode.key = tempKey
                currentNode.value = tempValue

            # If it has only one child
            else:
                if currentNode.hasLeftChild():
                    leftNode = currentNode.getLeftChild()
                    rebalancerNode = leftNode
                    if currentNode == self.root:
                        leftNode.parent = None
                        self.root = leftNode
                    else:
                        if currentNode.isLeftChild():
                            currentNode.parent.left = leftNode
                        elif currentNode.isRightChild():
                            currentNode.parent.right = leftNode
                        leftNode.parent = currentNode.parent
                else:
                    rightNode = currentNode.getRightChild()
                    rebalancerNode = rightNode
                    if currentNode == self.root:
                        rightNode.parent = None
                        self.root = rightNode
                    else:
                        if currentNode.isLeftChild():
                            currentNode.parent.left = rightNode
                        elif currentNode.isRightChild():
                            currentNode.parent.right = rightNode
                        rightNode.parent = currentNode.parent
            self.count -= 1
            if rebalancerNode:
                self.rebalance(rebalancerNode)

    def checkBalanceTopDown(self, node):
        if node:
            if abs(node.getBalanceFactor()) > 1:
                self.rebalance(node)
            elif node.hasAnyChildren():
                self.checkBalanceTopDown(node.getLeftChild())
                self.checkBalanceTopDown(node.getRightChild())

    def rebalance(self, node):
        #self.visualizeVertical()
        while node is not None:
            # it's right-heavy
            if node.getBalanceFactor() < -1:
                if node.hasRightChild() and node.getRightChild().getBalanceFactor() > 0:
                    self.rotateRight(node.getRightChild())
                self.rotateLeft(node)

            # it's left-heavy
            elif node.getBalanceFactor() > 1:
                if node.hasLeftChild() and node.getLeftChild().getBalanceFactor() < 0:
                    self.rotateLeft(node.getLeftChild())
                self.rotateRight(node)
            node = node.getParent()

    def rotateRight(self, node):
        oldNode = node
        newNode = node.getLeftChild()

        newNode.parent = oldNode.getParent()
        if oldNode.getParent():
            if oldNode.isLeftChild():
                oldNode.getParent().left = newNode
            else:
                oldNode.getParent().right = newNode
        else:
            self.root = newNode

        oldNode.parent = newNode
        oldNode.left = newNode.getRightChild()
        if oldNode.hasLeftChild():
            oldNode.getLeftChild().parent = oldNode
        newNode.right = oldNode
        #self.visualizeVertical()

    def rotateLeft(self, node):
        oldNode = node
        newNode = node.getRightChild()

        newNode.parent = oldNode.getParent()
        if newNode.getParent():
            if oldNode.isLeftChild():
                oldNode.getParent().left = newNode
            else:
                oldNode.getParent().right = newNode
        else:
            self.root = newNode

        oldNode.parent = newNode
        oldNode.right = newNode.getLeftChild()
        if oldNode.hasRightChild():
            oldNode.getRightChild().parent = oldNode
        newNode.left = oldNode
        #self.visualizeVertical()