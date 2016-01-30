class Deque(object):

    def __init__(self):
        self.__items = []

    def add_head(self, data):
        self.__items.insert(0, data)

    def add_tail(self, data):
        self.__items.append(data)

    def remove_head(self):
        if not self.is_empty():
            return self.__items.pop(0)

    def remote_tail(self):
        if not self.is_empty():
            return self.__items.pop()

    def peek_head(self):
        if not self.is_empty():
            return self.__items[0]

    def peek_tail(self):
        if not self.is_empty():
            return self.__items[self.size() - 1]

    def size(self):
        return len(self.__items)

    def is_empty(self):
        return True if self.size() == 0 else False

    def clear(self):
        self.__items = []
