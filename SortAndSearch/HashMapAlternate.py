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
        self.sizeOfTable = 16
        self.slots = [None] * self.sizeOfTable
        self.distributionTable = [0] * self.sizeOfTable
        for i in range(self.sizeOfTable):
            self.slots[i] = HashMapNode()

    def hash(self, key):
        return key % self.sizeOfTable

    def put(self, key, value):
        hashValue = self.hash(key)
        currentNode = self.slots[hashValue]
        done = False

        while not done:
            if currentNode.key == None: # case for first node
                currentNode.key = key
                currentNode.value = value
                self.distributionTable[hashValue] += 1
                done = True
            elif currentNode.key == key: # replace existing value for key
                currentNode.value = value
                done = True
            else:
                if currentNode.next is None: # add new pair to the end of list
                    currentNode.next = HashMapNode()
                    currentNode.next.key = key
                    currentNode.next.value = value
                    self.distributionTable[hashValue] += 1
                    done = True
                else: # move to the next node
                    currentNode = currentNode.next

    def get(self, key):
        hashValue = self.hash(key)
        currentNode = self.slots[hashValue]
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
        currentNode = self.slots[hashValue]
        previousNode = None
        done = False

        while not done:
            if currentNode.key == key:
                if previousNode is None: # we are at the beginning of the list
                    if currentNode.next is None:
                        self.slots[hashValue] = HashMapNode()
                    else:
                        self.slots[hashValue] = currentNode.next # change the links
                else:
                    previousNode.next = currentNode.next
                self.distributionTable[hashValue] -= 1
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
        for i in range(self.sizeOfTable):
            items = []
            currentNode = self.slots[i]

            while currentNode is not None:
                items.append(str(currentNode))
                currentNode = currentNode.next

            hashmapRepresentation.append(" -> ".join(items))
        return "\n".join(hashmapRepresentation)


hashMap = HashMapAlternate()
for i in range(128):
        hashMap.put(i, "ZZZ")
for i in range(128):
        hashMap.put(i, "YYY")
for i in range(128):
        hashMap.remove(i)
print(hashMap.distributionTable)
print(hashMap)
