class StackLLNode(object):
    

    def __init__(self, data, nextNode):
        self.data = data
        self.next = nextNode


# Linked list based Stack
class StackLL(object):

    def __init__(self):
        self.__top = None
        self.__count = 0

    def size(self):
        return self.__count

    def is_empty(self):
        return True if 0 >= self.size() else False

    def peek(self):
        return None if self.is_empty() else self.__top.data

    def pop(self):
        if not self.is_empty():
            holder = self.__top.data
            self.__top = self.__top.next
            self.__count -= 1
            return holder

    def push(self, data):
        newNode = StackLLNode(data, None)
        if self.is_empty():
            self.__top = newNode
        else:
            newNode.next = self.__top
            self.__top = newNode

        self.__count += 1

    def clear(self):
        self.__count = 0
        self.__top = None

    def __str__(self):
        contents = []
        if self.__count > 0:
            current = self.__top
            while current is not None:
                contents.append(current.data)
                current = current.next
            contents.reverse()
        return str(contents)


# Array based Stack
class StackAA(object):

    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def is_empty(self):
        return True if self.size() is 0 else False

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()

    def peek(self):
        return None if self.is_empty() else self.list[self.size() - 1]

    def clear(self):
        self.list = []

    def __str__(self):
        return str(self.list)


class StackAI(object):

    def __init__(self):
        self.list = []

    def is_empty(self):
        return True if self.size() is 0 else False

    def size(self):
        return len(self.list)

    def peek(self):
        return None if self.is_empty() else self.list[0]

    def push(self, data):
        self.list.insert(0,data)

    def pop(self):
        if not self.is_empty():
            return self.list.pop(0)

    def clear(self):
        self.list = []

    def __str__(self):
        contents = self.list
        contents.reverse()
        return str(contents)


