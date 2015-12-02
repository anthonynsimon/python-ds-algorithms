class Deque:
    def __init__(self):
        self.items = []

    def addHead(self, data):
        self.items.insert(0, data)

    def addTail(self, data):
        self.items.append(data)

    def removeHead(self):
        if self.isEmpty() == False:
            return self.items.pop(0)

    def removeTail(self):
        if self.isEmpty() == False:
            return self.items.pop()

    def peekHead(self):
        if self.isEmpty() == False:
            return self.items[0]

    def peekTail(self):
        if self.isEmpty() == False:
            return self.items[self.size()-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return True if self.size() == 0 else False

    def clear(self):
        self.items = []
