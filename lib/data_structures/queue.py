class QueueLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None


# Array based Queue
class QueueAA:

    def __init__(self):
        self.__front = None
        self.__back = None
        self.__list = []

    def enqueue(self, data):
        self.__list.insert(0, data)

    def dequeue(self):
        if not self.is_empty():
            return self.__list.pop()

    def is_empty(self):
        return False if len(self.__list) > 0 else True

    def size(self):
        return len(self.__list)

    def peek(self):
        if not self.is_empty():
            return self.__list[self.size() - 1]

    def clear(self):
        self.__front = None
        self.__back = None
        self.__list = []


# Linked list based Queue
class QueueLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        temp = QueueLLNode(data)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.count += 1

    def dequeue(self):
        if not self.is_empty():
            tempData  = self.head.data
            self.head = self.head.next
            self.count -= 1
            return tempData

    def is_empty(self):
        return False if self.count > 0 else True

    def size(self):
        return self.count

    def peek(self):
        if not self.is_empty():
            return self.head.data

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
