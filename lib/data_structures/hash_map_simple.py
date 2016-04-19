# TODO:
# + Make Linked List based collision resolution
# + Write unit Tests
# + Add "remove" method

class HashMapSimple(object):

    def __init__(self):
        self.__table_size = 64
        self.__slots = [None] * self.__table_size
        self.__data = [None] * self.__table_size

    def hash(self, key):
        if type(key) is str:
            sum = 0
            position = 1
            for ch in key:
                sum += ord(ch) * position
            key = sum
        return key % self.__table_size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.__table_size

    def put(self, key, value):
        hash_value = self.hash(key)
        done = False
        for i in range(self.__table_size):
            if self.__slots[hash_value] == None:
                self.__slots[hash_value] = key
                self.__data[hash_value] = value
                done = True
                break
            elif self.__slots[hash_value] == key:
                self.__data[hash_value] = value
                done = True
                break
            else:
                hash_value = self.rehash(hash_value)

    def get(self, key):
        hash_value = self.hash(key)
        found = False
        for i in range(self.__table_size):
            if self.__slots[hash_value] == key:
                found = True
                break
            else:
                hash_value = self.rehash(hash_value)

        if found:
            return self.__data[hash_value]
        else:
            return False
