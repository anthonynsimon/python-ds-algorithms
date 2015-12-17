# TODO:
# + Write unit tests
# + Change to an ordered list in each slot to enable use of binary search
# + If possible reuse methods for moving through the slot lists

class HashMapNode(object):

    def __init__(self):
        self.key = None
        self.value = None
        self.next = None

    def __repr__(self):
        return "[Key: {0}, Value: {1}]".format(self.key, self.value)

class HashMapAlternate(object):

    def __init__(self):
        self.__sizeOfTable = 64
        self.__slots = [None] * self.__sizeOfTable
        self.__distributionTable = [0] * self.__sizeOfTable
        for i in range(self.__sizeOfTable):
            self.__slots[i] = HashMapNode()

    def hash(self, key):
        if type(key) is str:
            sum = 0
            position = 1
            for ch in key:
                sum += ord(ch) * position
                position += 1
            key = sum

        return key % self.__sizeOfTable

    def put(self, key, value):
        hashValue = self.hash(key)
        currentNode = self.__slots[hashValue]
        done = False
        while not done:
            if currentNode.key == None: # case for first node
                currentNode.key = key
                currentNode.value = value
                self.__distributionTable[hashValue] += 1
                done = True
            elif currentNode.key == key: # replace existing value for key
                currentNode.value = value
                done = True
            else:
                if currentNode.next is None: # add new pair to the end of list
                    currentNode.next = HashMapNode()
                    currentNode.next.key = key
                    currentNode.next.value = value
                    self.__distributionTable[hashValue] += 1
                    done = True
                else: # move to the next node
                    currentNode = currentNode.next

    def get(self, key):
        hashValue = self.hash(key)
        currentNode = self.__slots[hashValue]
        done = False
        while not done:
            if currentNode.key == key: # we found the key
                done = True
            elif currentNode.next is not None:
                currentNode = currentNode.next # keep moving through the list
            else:
                break # we reached the end of the list

        if done:
            return currentNode.value
        else:
            return False

    def remove(self, key):
        hashValue = self.hash(key)
        currentNode = self.__slots[hashValue]
        previousNode = None
        done = False
        while not done:
            if currentNode.key == key:
                if previousNode is None: # we are at the beginning of the list
                    if currentNode.next is None:
                        self.__slots[hashValue] = HashMapNode()
                    else:
                        self.__slots[hashValue] = currentNode.next # change the links
                else:
                    previousNode.next = currentNode.next
                self.__distributionTable[hashValue] -= 1
                done = True
            elif currentNode.next is not None:
                previousNode = currentNode
                currentNode = currentNode.next # keep moving through the list
            else:
                break # we reached the end of the list

        if done:
            return currentNode.value
        else:
            return False

    def __repr__(self):
        hashmapRepresentation = []
        for i in range(self.__sizeOfTable):
            items = []
            currentNode = self.__slots[i]
            while currentNode is not None:
                items.append(str(currentNode))
                currentNode = currentNode.next
            hashmapRepresentation.append(" -> ".join(items))
        return "\n".join(hashmapRepresentation)
