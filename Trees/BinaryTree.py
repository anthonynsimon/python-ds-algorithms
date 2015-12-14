class BinaryTree(object):
    def __init__(self, rootKey):
        self.rootKey = rootKey
        self.leftChild = None
        self.rightChild = None

    def insertLeftChild(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            branch = BinaryTree(newNode)
            branch.leftChild = self.leftChild
            self.leftChild = branch

    def insertRightChild(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            branch = BinaryTree(newNode)
            branch.rightChild = self.rightChild
            self.rightChild = branch

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootKey(self, rootKey):
        self.rootKey = rootKey

    def getRootKey(self):
        return self.rootKey

    def __repr__(self):
        return str(self.traversePreorder(self))

    def traversePreorder(self, tree):
        items = [tree.getRootKey()]

        leftChild = tree.getLeftChild()
        rightChild = tree.getRightChild()

        if leftChild:
            items.append(self.traversePreorder(leftChild))
        if rightChild:
            items.append(self.traversePreorder(rightChild))

        return items

    def traverseInorder(self, tree):
        leftChild = tree.getLeftChild()
        rightChild = tree.getRightChild()
        items = []

        if leftChild:
            items.append(self.traverseInorder(leftChild))

        items.append(tree.getRootKey())

        if rightChild:
            items.append(self.traverseInorder(rightChild))

        return items

    def traversePostorder(self, tree):
        leftChild = tree.getLeftChild()
        rightChild = tree.getRightChild()
        items = []

        if leftChild:
            items.append(self.traversePostorder(leftChild))
        if rightChild:
            items.append(self.traversePostorder(rightChild))

        items.append(tree.getRootKey())
        return items