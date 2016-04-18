class BinaryTree(object):
    def __init__(self, rootKey):
        self.__rootKey = rootKey
        self.__leftChild = None
        self.__rightChild = None

    def insertLeftChild(self, newNode):
        if self.__leftChild is None:
            self.__leftChild = BinaryTree(newNode)
        else:
            branch = BinaryTree(newNode)
            branch.__leftChild = self.__leftChild
            self.__leftChild = branch

    def insertRightChild(self, newNode):
        if self.__rightChild is None:
            self.__rightChild = BinaryTree(newNode)
        else:
            branch = BinaryTree(newNode)
            branch.__rightChild = self.__rightChild
            self.__rightChild = branch

    def getLeftChild(self):
        return self.__leftChild

    def getRightChild(self):
        return self.__rightChild

    def setRootKey(self, rootKey):
        self.__rootKey = rootKey

    def getRootKey(self):
        return self.__rootKey

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