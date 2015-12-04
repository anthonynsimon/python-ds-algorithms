class Deque(object):
    def __init__(self):
        self.items = []

    def addHead(self, data):
        self.items.insert(0, data)

    def addTail(self, data):
        self.items.append(data)

    def removeHead(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def removeTail(self):
        if not self.isEmpty():
            return self.items.pop()

    def peekHead(self):
        if not self.isEmpty():
            return self.items[0]

    def peekTail(self):
        if not self.isEmpty():
            return self.items[self.size()-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def clear(self):
        self.items = []
