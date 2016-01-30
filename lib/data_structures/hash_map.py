class HashMapNode(object):

    def __init__(self):
        self.key = None
        self.value = None
        self.next = None

    def __repr__(self):
        return "[Key: {0}, Value: {1}]".format(self.key, self.value)

class HashMap(object):

    def __init__(self):
        self.__size = 64
        self.__slots = [None] * self.__size
        self.__distribution_table = [0] * self.__size
        for i in range(self.__size):
            self.__slots[i] = HashMapNode()

    def hash(self, key):
        if type(key) is str:
            sum = 0
            position = 1
            for ch in key:
                sum += ord(ch) * position
                position += 1
            key = sum

        return key % self.__size

    def put(self, key, value):
        hash_value = self.hash(key)
        current_node = self.__slots[hash_value]
        done = False
        while not done:
            if current_node.key == None: # case for first node
                current_node.key = key
                current_node.value = value
                self.__distribution_table[hash_value] += 1
                done = True
            elif current_node.key == key: # replace existing value for key
                current_node.value = value
                done = True
            else:
                if current_node.next is None: # add new pair to the end of list
                    current_node.next = HashMapNode()
                    current_node.next.key = key
                    current_node.next.value = value
                    self.__distribution_table[hash_value] += 1
                    done = True
                else: # move to the next node
                    current_node = current_node.next

    def get(self, key):
        hash_value = self.hash(key)
        current_node = self.__slots[hash_value]
        done = False
        while not done:
            if current_node.key == key: # we found the key
                done = True
            elif current_node.next is not None:
                current_node = current_node.next # keep moving through the list
            else:
                break # we reached the end of the list

        if done:
            return current_node.value
        else:
            return False

    def remove(self, key):
        hash_value = self.hash(key)
        current_node = self.__slots[hash_value]
        previous_node = None
        done = False
        while not done:
            if current_node.key == key:
                if previous_node is None: # we are at the beginning of the list
                    if current_node.next is None:
                        self.__slots[hash_value] = HashMapNode()
                    else:
                        self.__slots[hash_value] = current_node.next # change the links
                else:
                    previous_node.next = current_node.next
                self.__distribution_table[hash_value] -= 1
                done = True
            elif current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next # keep moving through the list
            else:
                break # we reached the end of the list

        if done:
            return current_node.value
        else:
            return False

    def __repr__(self):
        hash_map_repr = []
        for i in range(self.__size):
            items = []
            current = self.__slots[i]
            while current is not None:
                items.append(str(current))
                current = current.next
            hash_map_repr.append(" -> ".join(items))
        return "\n".join(hash_map_repr)
