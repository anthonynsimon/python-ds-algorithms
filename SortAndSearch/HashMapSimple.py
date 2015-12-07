# TODO:
# + Add string key or generic style keys
# + Make Linked List based collision resolution

class HashMapSimple(object):
    def __init__(self):
        self.sizeOfTable = 16
        self.slots = [None] * self.sizeOfTable
        self.data = [None] * self.sizeOfTable

    def hash(self, key):
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

hashMap = HashMapSimple()
for i in range(16):
    hashMap.put(i,"Something")
for i in range(16,32):
    hashMap.put(i,"Break")
print(hashMap.slots)
print(hashMap.data)