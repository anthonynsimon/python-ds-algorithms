class Deque(object):

    def __init__(self):
        self.__items = []

    def addHead(self, data):
        self.__items.insert(0, data)

    def addTail(self, data):
        self.__items.append(data)

    def removeHead(self):
        if not self.isEmpty():
            return self.__items.pop(0)

    def removeTail(self):
        if not self.isEmpty():
            return self.__items.pop()

    def peekHead(self):
        if not self.isEmpty():
            return self.__items[0]

    def peekTail(self):
        if not self.isEmpty():
            return self.__items[self.size() - 1]

    def size(self):
        return len(self.__items)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def clear(self):
        self.__items = []
