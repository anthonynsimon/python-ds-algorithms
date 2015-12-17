class BinaryHeap(object):

    def __init__(self):
        self.__heapList = [0]
        self.__count = 0

    def insert(self, value):
        self.__heapList.append(value)
        self.__count += 1
        self.percolateUp(self.size())

    def findMin(self):
        if not self.isEmpty():
            return self.__heapList[1]

    def deleteMin(self):
        if not self.isEmpty():
            if self.size() == 1:
                self.__heapList.pop()
                self.__count -= 1
            else:
                self.__heapList[1] = self.__heapList.pop()
                self.__count -= 1
                self.percolateDown(1)

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.__count

    # if we already have the entire list we can just place it after "[0]"
    # and simply percolate down while moving the index "up" the heap to
    # accommodate the values along the way
    # STOP <== (Index -= 1)
    # [0, A, B, C, D, E]
    def buildHeap(self, fromList):
        if type(fromList) is list:
            self.clear()
            self.__heapList.extend(fromList)
            self.__count = len(fromList)
            index = self.size() // 2
            while index > 0:
                self.percolateDown(index)
                index -= 1

    def clear(self):
        self.__heapList = [0]
        self.__count = 0

    def percolateUp(self, index):
        while index // 2 > 0:
            if self.__heapList[index] < self.__heapList[index // 2]:
                self.swapContents(index, index // 2, self.__heapList)
            index //= 2

    def percolateDown(self, index):
        while index * 2 <= self.size(): # while it has at least one child
            minChild = self.minimumChild(index)
            if self.__heapList[minChild] < self.__heapList[index]:
                self.swapContents(minChild, index, self.__heapList)
            index = minChild

    def minimumChild(self, index):
        leftChild = index * 2
        rightChild = index * 2 + 1
        if rightChild > self.size():
            return leftChild
        else:
            if self.__heapList[leftChild] < self.__heapList[rightChild]:
                return leftChild
            else:
                return rightChild

    def swapContents(self, indexA, indexB, inList):
        inList[indexA], inList[indexB] = inList[indexB], inList[indexA]

    def __repr__(self):
        return str(self.__heapList)