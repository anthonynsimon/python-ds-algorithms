class BinarySearch(object):

    def __init__(self):
        self.steps = 0

    def containsValue(self, value, numbers):
        found = self.containsValueRecursiveWorker(value, numbers)
        result = ""

        if found:
            result = "List contains value. Took {0} steps.".format(self.steps)
        else:
            result = "List doesn't contain value. Took {0} steps.".format(self.steps)
        self.steps = 0
        return result

    def containsValueWorker(self, value, numbers):
        size = len(numbers)
        if size == 0 or value > numbers[size-1]:
            return False

        while size > 1:
            self.steps += 1
            size = len(numbers)
            middle = size//2
            if value == numbers[middle]:
                return True
                break
            elif value > numbers[middle]:
                numbers = numbers[size//2:size]
            elif value < numbers[middle]:
                numbers = numbers[0:size//2]
        return False

    def containsValueRecursiveWorker(self, value, numbers):
        self.steps += 1
        size = len(numbers)
        if size == 0 or value > numbers[size-1]:
            return False

        if value == numbers[size//2]:
            return True
        elif value < numbers[size//2]:
            return self.containsValueRecursiveWorker(value, numbers[0:size//2])
        elif value > numbers[size//2]:
            return self.containsValueRecursiveWorker(value, numbers[size//2:size])


numbers = []
for i in range(10000000):
    numbers.append(i)

search = BinarySearch()
print(search.containsValue(924681, numbers))