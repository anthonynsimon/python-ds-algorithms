# TODO:
# + Make Linked List based collision resolution
# + Write unit Tests
# + Add "remove" method

class HashMapSimple(object):

    def __init__(self):
        self.__sizeOfTable = 64
        self.__slots = [None] * self.__sizeOfTable
        self.__data = [None] * self.__sizeOfTable

    def hash(self, key):
        if type(key) is str:
            sum = 0
            position = 1
            for ch in key:
                sum += ord(ch) * position
            key = sum
        return key % self.__sizeOfTable

    def rehash(self, oldHash):
        return (oldHash + 1) % self.__sizeOfTable

    def put(self, key, value):
        hashValue = self.hash(key)
        done = False
        for i in range(self.__sizeOfTable):
            if self.__slots[hashValue] == None:
                self.__slots[hashValue] = key
                self.__data[hashValue] = value
                done = True
                break
            elif self.__slots[hashValue] == key:
                self.__data[hashValue] = value
                done = True
                break
            else:
                hashValue = self.rehash(hashValue)

    def get(self, key):
        hashValue = self.hash(key)
        found = False
        for i in range(self.__sizeOfTable):
            if self.__slots[hashValue] == key:
                found = True
                break
            else:
                hashValue = self.rehash(hashValue)

        if found:
            return self.__data[hashValue]
        else:
            return False
