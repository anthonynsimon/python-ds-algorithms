class BinarySearch(object):

    def __init__(self):
        self.steps = 0

    def contains_value(self, value, numbers):
        found = self.__search_helper_recursive(value, numbers)
        result = ""

        if found:
            result = "List contains value. Took {0} steps.".format(self.steps)
        else:
            result = "List doesn't contain value. Took {0} steps.".format(self.steps)
        self.steps = 0
        return result

    def __search_helper(self, value, numbers):
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

    def __search_helper_recursive(self, value, numbers):
        self.steps += 1
        size = len(numbers)
        if size == 0 or value > numbers[size-1]:
            return False

        if value == numbers[size // 2]:
            return True
        elif value < numbers[size // 2]:
            return self.__search_helper_recursive(value, numbers[0:size // 2])
        elif value > numbers[size // 2]:
            return self.__search_helper_recursive(value, numbers[size // 2:size])


numbers = []
for i in range(10000000):
    numbers.append(i)

search = BinarySearch()
print(search.contains_value(924681, numbers))