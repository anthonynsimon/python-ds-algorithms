from DataStructures.Trees import BinarySearchTree

class AVLNode(BinarySearchTree.BSTNode):
    def getBalanceFactor(self):
        balanceFactor = 0
        if self.hasLeftChild():
            balanceFactor -= self.getLeftChild().getSubtreeSize()
        if self.hasRightChild():
            balanceFactor += self.getRightChild().getSubtreeSize()
        return balanceFactor


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
                        currentNode.leftChild = AVLNode(key,value,None,None,currentNode)
                        done = True
                elif currentNode.key < key:
                    if currentNode.hasRightChild():
                        currentNode = currentNode.getRightChild()
                    else:
                        currentNode.rightChild = AVLNode(key,value,None,None,currentNode)
                        done = True
            self.count += 1
            self.checkBalance(currentNode)

    def remove(self, key):
        nodeToRemove = self.get(key)
        if nodeToRemove:
            # If it has no children
            if nodeToRemove.isLeaf():
                if nodeToRemove.isRoot():
                    self.root = None
                elif nodeToRemove == nodeToRemove.parent.getLeftChild():
                    nodeToRemove.parent.leftChild = None
                else:
                    nodeToRemove.parent.rightChild = None

            # If it has both children
            elif nodeToRemove.hasBothChildren():
                successorNode = self.getSuccessor(nodeToRemove)
                tempKey = successorNode.key
                tempValue = successorNode.value
                self.remove(successorNode.key) # must clear it before changing the BST path
                nodeToRemove.key = tempKey
                nodeToRemove.value = tempValue

            # If it has only one child
            else:
                if nodeToRemove.hasLeftChild():
                    leftNode = nodeToRemove.getLeftChild()
                    if nodeToRemove == self.root:
                        leftNode.parent = None
                        self.root = leftNode
                    else:
                        if nodeToRemove.isLeftChild():
                            nodeToRemove.parent.leftChild = leftNode
                        elif nodeToRemove.isRightChild():
                            nodeToRemove.parent.rightChild = leftNode
                        leftNode.parent = nodeToRemove.parent
                else:
                    rightNode = nodeToRemove.getRightChild()
                    if nodeToRemove == self.root:
                        rightNode.parent = None
                        self.root = rightNode
                    else:
                        if nodeToRemove.isLeftChild():
                            nodeToRemove.parent.leftChild = rightNode
                        elif nodeToRemove.isRightChild():
                            nodeToRemove.parent.rightChild = rightNode
                        rightNode.parent = nodeToRemove.parent
            self.count -= 1
            self.checkBalance(self.getMax())

    def checkBalance(self, node):
        if node:
            if abs(node.getBalanceFactor()) > 1:
                self.rebalance(node)
            else:
                self.checkBalance(node.getParent())

    def rebalance(self, node):
        #self.visualizeVertical()
        # unbalanced towards right
        if node.getBalanceFactor() > 1:
            if node.hasLeftChild() and node.getLeftChild().getBalanceFactor() < 0:
                self.rotateRight(node.getLeftChild())
            self.rotateLeft(node)

        # unbalanced towards left
        if node.getBalanceFactor() < -1:
            if node.hasRightChild() and node.getRightChild().getBalanceFactor() > 0:
                self.rotateLeft(node.getRightChild())
            self.rotateRight(node)

    def rotateRight(self, node):
        oldParent = node
        newParent = node.getLeftChild()

        newParent.parent = oldParent.getParent()
        if oldParent.getParent():
            if oldParent.isLeftChild():
                newParent.getParent().leftChild = newParent
            else:
                newParent.getParent().rightChild = newParent
        else:
            self.root = newParent

        oldParent.parent = newParent
        oldParent.leftChild = newParent.getRightChild()
        if oldParent.hasLeftChild():
            oldParent.getLeftChild().parent = oldParent
        newParent.rightChild = oldParent

    def rotateLeft(self, node):
        oldParent = node
        newParent = node.getRightChild()

        newParent.parent = oldParent.getParent()
        if oldParent.getParent():
            if oldParent.isLeftChild():
                newParent.getParent().leftChild = newParent
            else:
                newParent.getParent().rightChild = newParent
        else:
            self.root = newParent

        oldParent.parent = newParent
        oldParent.rightChild = newParent.getLeftChild()
        if oldParent.hasRightChild():
            oldParent.getRightChild().parent = oldParent
        newParent.leftChild = oldParent