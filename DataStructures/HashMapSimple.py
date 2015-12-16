# TODO:
# + Make Linked List based collision resolution
# + Write unit Tests
# + Add "remove" method

class HashMapSimple(object):

    def __init__(self):
        self.sizeOfTable = 64
        self.slots = [None] * self.sizeOfTable
        self.data = [None] * self.sizeOfTable

    def hash(self, key):
        if type(key) is str:
            sum = 0
            position = 1
            for ch in key:
                sum += ord(ch) * position
            key = sum
        return key % self.sizeOfTable

    def rehash(self, oldHash):
        return (oldHash + 1) % self.sizeOfTable

    def put(self, key, value):
        hashValue = self.hash(key)
        done = False
        for i in range(self.sizeOfTable):
            if self.slots[hashValue] == None:
                self.slots[hashValue] = key
                self.data[hashValue] = value
                done = True
                break
            elif self.slots[hashValue] == key:
                self.data[hashValue] = value
                done = True
                break
            else:
                hashValue = self.rehash(hashValue)

    def get(self, key):
        hashValue = self.hash(key)
        found = False
        for i in range(self.sizeOfTable):
            if self.slots[hashValue] == key:
                found = True
                break
            else:
                hashValue = self.rehash(hashValue)

        if found:
            return self.data[hashValue]
        else:
            return False
