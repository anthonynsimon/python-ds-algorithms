# TODO
# Create AVL Tree based on this one

class BSTNode(object):

    def __init__(self, key, value=None, leftChild=None, rightChild=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def isLeaf(self):
        return self.hasAnyChildren() is False

    def isRoot(self):
        return self.parent == None

    def isLeftChild(self):
        if self.parent:
            return self.parent.getLeftChild() == self
        return False

    def isRightChild(self):
        if self.parent:
            return self.parent.getRightChild() == self
        return False

    def hasAnyChildren(self):
        return self.hasLeftChild() or self.hasRightChild()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def getLeftChild(self):
        if self.hasLeftChild():
            return self.leftChild

    def getRightChild(self):
        if self.hasRightChild():
            return self.rightChild

    def getParent(self):
        if not self.isRoot():
            return self.parent

    def replaceContentsInPlace(self, key, value=None, leftChild=None, rightChild=None, parent=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def __repr__(self):
        return "'{0}' : {1}".format(self.key,self.value)
        #return "{0}".format(self.key)

    def __iter__(self):
        if self.hasLeftChild():
            yield self.leftChild
        if self.hasRightChild():
            yield self.rightChild


class BinarySearchTree(object):

    def __init__(self):
        self.__root = None
        self.__count = 0

    def put(self, key, value):
        if self.__root is None:
            self.__root = BSTNode(key, value)
            self.__count = 1
        else:
            currentNode = self.__root
            done = False
            while not done:
                if currentNode.key == key:
                    currentNode.value = value
                    done = True
                elif currentNode.key > key:
                    if currentNode.hasLeftChild():
                        currentNode = currentNode.getLeftChild()
                    else:
                        currentNode.leftChild = BSTNode(key,value,None,None,currentNode)
                        done = True
                elif currentNode.key < key:
                    if currentNode.hasRightChild():
                        currentNode = currentNode.getRightChild()
                    else:
                        currentNode.rightChild = BSTNode(key,value,None,None,currentNode)
                        done = True
            self.__count += 1

    def get(self, key):
        if key is not None:
            currentNode = self.__root
        done = False
        while not done:
            if currentNode.key == key:
                done = True
            elif currentNode.hasAnyChildren():
                if currentNode.key > key:
                    if currentNode.hasLeftChild():
                        currentNode = currentNode.getLeftChild()
                    else:
                        done = True
                elif currentNode.key < key:
                    if currentNode.hasRightChild():
                        currentNode = currentNode.getRightChild()
                    else:
                        done = True
            else:
                done = True

        if currentNode.key == key:
            return currentNode
        return None

    def remove(self, key):
        nodeToRemove = self.get(key)
        if nodeToRemove:
            # If it has no children
            if nodeToRemove.isLeaf():
                if nodeToRemove == self.__root:
                    nodeToRemove = None
                elif nodeToRemove == nodeToRemove.parent.getLeftChild():
                    nodeToRemove.parent.leftChild = None
                else:
                    nodeToRemove.parent.rightChild = None

            # If it has both children
            elif nodeToRemove.hasBothChildren():
                successorNode = self.__getSuccessor(nodeToRemove)
                tempKey = successorNode.key
                tempValue = successorNode.value
                self.remove(successorNode.key) # must clear it before changing the BST path
                nodeToRemove.key = tempKey
                nodeToRemove.value = tempValue

            # If it has only one child
            else:
                if nodeToRemove.hasLeftChild():
                    leftNode = nodeToRemove.getLeftChild()
                    if nodeToRemove == self.__root:
                        leftNode.parent = None
                        self.__root = leftNode
                    else:
                        if nodeToRemove.isLeftChild():
                            nodeToRemove.parent.leftChild = leftNode
                        elif nodeToRemove.isRightChild():
                            nodeToRemove.parent.rightChild = leftNode
                        leftNode.parent = nodeToRemove.parent
                else:
                    rightNode = nodeToRemove.getRightChild()
                    if nodeToRemove == self.__root:
                        rightNode.parent = None
                        self.__root = rightNode
                    else:
                        if nodeToRemove.isLeftChild():
                            nodeToRemove.parent.leftChild = rightNode
                        elif nodeToRemove.isRightChild():
                            nodeToRemove.parent.rightChild = rightNode
                        rightNode.parent = nodeToRemove.parent
            self.__count -= 1

    def getMin(self):
        if self.__root:
            currentNode = self.__root
            while currentNode.hasLeftChild():
                currentNode = currentNode.getLeftChild()
            return currentNode

    def getMax(self):
        if self.__root:
            currentNode = self.__root
            while currentNode.hasRightChild():
                currentNode = currentNode.getRightChild()
            return currentNode

    def __getSuccessor(self, startingNode):
        successorNode = startingNode.getRightChild()
        while successorNode.hasLeftChild():
            successorNode = successorNode.getLeftChild()
        return successorNode

    def __getitem__(self, item):
        result =  self.get(item)
        if result:
            return result.value

    def __setitem__(self, key, value):
        self.put(key,value)

    def __delitem__(self, key):
        self.remove(key)

    def __len__(self):
        return self.__count

    def __contains__(self, key):
        if self.get(key):
            return True

    def __repr__(self):
        if self.__root is not None and type(self.__root) is BSTNode:
            items = []
            self.reprHelper(self.__root, items)
            return str(items)
        return "[]"

    def __iter__(self):
        if self.__root:
            startNode = self.__root
            items = []
            self.iterHelper(startNode, items)
            for item in items:
                yield item

    def iterHelper(self, node, items):
        if node.hasLeftChild():
            self.iterHelper(node.getLeftChild(), items)
        items.append(node)
        if node.hasRightChild():
            self.iterHelper(node.getRightChild(), items)


    def reprHelper(self, node, items):
        if node:
            if node.hasLeftChild():
                self.reprHelper(node.getLeftChild(), items)
            items.append(node)
            if node.hasRightChild():
                self.reprHelper(node.getRightChild(), items)

    def visualize(self, level=0, node=None):
        if node is None:
            node = self.__root
        adder = "Root = "
        if node.isLeftChild():
            adder = "Left = "
        elif node.isRightChild():
            adder = "Right = "
        print ('\t' * level + adder + repr(node))
        for child in node:
            self.visualize(level + 1, child)