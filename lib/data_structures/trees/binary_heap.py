class BinaryHeap(object):

    def __init__(self):
        self.__heap = [0]
        self.__count = 0

    def insert(self, value):
        self.__heap.append(value)
        self.__count += 1
        self.percolate_up(self.size())

    def find_min(self):
        if not self.is_empty():
            return self.__heap[1]

    def delete_min(self):
        if not self.is_empty():
            if self.size() == 1:
                result = self.__heap.pop()
                self.__count -= 1
                return result
            else:
                result = self.__heap[1]
                self.__heap[1] = self.__heap.pop()
                self.__count -= 1
                self.percolate_down(1)
                return result

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__count

    # if we already have the entire list we can just place it after "[0]"
    # and simply percolate down while moving the index "up" the heap to
    # accommodate the values along the way
    # STOP <== (Index -= 1)
    # [0, A, B, C, D, E]
    def build_heap(self, data):
        if type(data) is list:
            self.clear()
            self.__heap.extend(data)
            self.__count = len(data)
            index = self.size() // 2
            while index > 0:
                self.percolate_down(index)
                index -= 1

    def clear(self):
        self.__heap = [0]
        self.__count = 0

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.__heap[index] < self.__heap[index // 2]:
                self.swap_contents(index, index // 2, self.__heap)
            index //= 2

    def percolate_down(self, index):
        while index * 2 <= self.size(): # while it has at least one child
            min_child = self.get_min_child(index)
            if self.__heap[min_child] < self.__heap[index]:
                self.swap_contents(min_child, index, self.__heap)
            index = min_child

    def get_min_child(self, index):
        left = index * 2
        right = index * 2 + 1
        if right > self.size():
            return left
        else:
            if self.__heap[left] < self.__heap[right]:
                return left
            else:
                return right

    def swap_contents(self, index_a, index_b, items):
        items[index_a], items[index_b] = items[index_b], items[index_a]

    def rebuild_heap(self):
        self.build_heap(self.__heap[1:])

    def __repr__(self):
        return str(self.__heap[1:])