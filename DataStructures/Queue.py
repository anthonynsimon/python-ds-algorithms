class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class ALQueue:
    def __init__(self):
        self.front = None
        self.back = None
        self.list = []

    def enqueue(self, data):
        self.list.insert(0, data)

    def dequeue(self):
        if not self.isEmpty():
            return self.list.pop()

    def isEmpty(self):
        return False if len(self.list) > 0 else True

    def size(self):
        return len(self.list)

    def peek(self):
        if not self.isEmpty():
            return self.list[self.size()-1]

    def clear(self):
        self.front = None
        self.back = None
        self.list = []


class LLQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        temp = LLNode(data)
        if self.isEmpty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.count += 1

    def dequeue(self):
        if not self.isEmpty():
            tempData  = self.head.data
            self.head = self.head.next
            self.count -= 1
            return tempData

    def isEmpty(self):
        return False if self.count > 0 else True

    def size(self):
        return self.count

    def peek(self):
        if not self.isEmpty():
            return self.head.data

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
