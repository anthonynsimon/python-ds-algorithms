class BinaryHeap(object):

    def __init__(self):
        self.heapList = [0]
        self.count = 0

    def insert(self, value):
        self.heapList.append(value)
        self.count += 1
        self.percolateUp(self.count)

    def findMin(self):
        if not self.isEmpty():
            return self.heapList[1]

    def deleteMin(self):
        if not self.isEmpty():
            if self.size() == 1:
                self.heapList.pop()
                self.count -= 1
            else:
                self.heapList[1] = self.heapList.pop()
                self.count -= 1
                self.percolateDown(1)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.count

    # if we already have the entire list we can just place it after "[0]"
    # and simply percolate down while moving the index "up" the heap to
    # accommodate the values along the way
    # STOP <== (Index -= 1)
    # [0, A, B, C, D, E]
    def buildHeap(self, fromList):
        if type(fromList) is list:
            self.clear()
            self.heapList.extend(fromList)
            self.count = len(fromList)
            index = self.count // 2
            while index > 0:
                self.percolateDown(index)
                index -= 1

    def clear(self):
        self.heapList = [0]
        self.count = 0

    def percolateUp(self, index):
        while index // 2 > 0:
            if self.heapList[index] < self.heapList[index // 2]:
                self.swapContents(index, index // 2, self.heapList)
            index //= 2

    def percolateDown(self, index):
        while index * 2 <= self.size(): # while it has at least one child
            minChild = self.minimumChild(index)
            if self.heapList[minChild] < self.heapList[index]:
                self.swapContents(minChild, index, self.heapList)
            index = minChild

    def minimumChild(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        if rightChild > self.size():
            return leftChild
        else:
            if self.heapList[leftChild] < self.heapList[rightChild]:
                return leftChild
            else:
                return rightChild

    def swapContents(self, indexA, indexB, inList):
        inList[indexA], inList[indexB] = inList[indexB], inList[indexA]

    def __repr__(self):
        return str(self.heapList)