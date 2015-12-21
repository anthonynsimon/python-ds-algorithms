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

    def getSubtreeSize(self):
        leftSize = 0
        rightSize = 0
        if self.hasLeftChild():
            leftSize += self.getLeftChild().getSubtreeSize()
        if self.hasRightChild():
            rightSize += self.getRightChild().getSubtreeSize()
        return 1 + leftSize + rightSize

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
        self.root = None
        self.count = 0

    def put(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
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
                        currentNode.leftChild = BSTNode(key,value,None,None,currentNode)
                        done = True
                elif currentNode.key < key:
                    if currentNode.hasRightChild():
                        currentNode = currentNode.getRightChild()
                    else:
                        currentNode.rightChild = BSTNode(key,value,None,None,currentNode)
                        done = True
            self.count += 1

    def get(self, key):
        if key is not None:
            currentNode = self.root
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
                if nodeToRemove == self.root:
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

    def getMin(self):
        if self.root:
            currentNode = self.root
            while currentNode.hasLeftChild():
                currentNode = currentNode.getLeftChild()
            return currentNode

    def getMax(self):
        if self.root:
            currentNode = self.root
            while currentNode.hasRightChild():
                currentNode = currentNode.getRightChild()
            return currentNode

    def getSuccessor(self, startingNode):
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
        return self.count

    def __contains__(self, key):
        if self.get(key):
            return True

    def __repr__(self):
        if self.root is not None:
            def reprHelper(node, items):
                if node:
                    if node.hasLeftChild():
                        reprHelper(node.getLeftChild(), items)
                    items.append(node)
                    if node.hasRightChild():
                        reprHelper(node.getRightChild(), items)
            items = []
            reprHelper(self.root, items)
            return str(items)
        return "[]"

    def __iter__(self):
        if self.root:
            startNode = self.root
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

    def visualizeHorizontal(self, level=0, node=None):
        if node is None:
            node = self.root
        adder = "Root = "
        if node.isLeftChild():
            adder = "Left = "
        elif node.isRightChild():
            adder = "Right = "
        print ('\t' * level + adder + repr(node))
        for child in node:
            self.visualize(level + 1, child)

    def visualizeVertical(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.getLeftChild())
            right_lines, right_pos, right_width = recurse(node.getRightChild())
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.getLeftChild() and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        print '\n'.join(recurse(self.root)[0])