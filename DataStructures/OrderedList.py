class OrderedListNode(object):

    def __init__(self, initData):
        self.data = initData
        self.next = None

class OrderedList(object):

    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, item):
        if self.head == None:
            self.head = OrderedListNode(item)
        else:
            current = self.head
            previous = None
            done = False
            newNode = OrderedListNode(item)
            while not done:
                if current is None:
                    done = True
                else:
                    if current.data > item:
                        done = True
                    else:
                        previous = current
                        current = current.next

            if previous is None:
                newNode.next = self.head
                self.head = newNode
            else:
                previous.next = newNode
                newNode.next = current
        self.count += 1

    def remove(self, item):
        done = False
        current = self.head
        previous = None
        while done == False:
            if current == None:
                print("Couldn't find item '{0}'" .format(item))
                done = True
            else:
                if item == current.data:
                    self.count -= 1
                    if previous == None:
                        self.head = current.next
                    else:
                        previous.next = current.next
                    done = True
                else:
                    previous = current
                    current = current.next


    def search(self, item):
        found = False
        current = self.head
        while current is not None:
            if item == current.data:
                found = True
                break
            else:
                current = current.next
        return found

    def isEmpty(self):
        return True if self.size() == 0 else False

    def size(self):
        return self.count

    def pop(self):
        done = False
        current = self.head
        if self.isEmpty():
            return

        if self.size() == 1:
            temp  = self.head.data
            self.head = None
            self.count -= 1
            return temp
        else:
            while current.next.next is not None:
                current = current.next
            temp = current.next.data
            current.next = None
            self.count -= 1
            return temp

    def clear(self):
        self.head = None
        self.count = 0

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return str(nodes)
