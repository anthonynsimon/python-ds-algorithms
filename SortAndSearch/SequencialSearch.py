class SequentialSearch(object):

    def containsValue(self, value, list):
        if len(list) == 0:
            return False

        found = False
        steps = 0
        for i in range(len(list)):
            steps += 1
            if list[i] == value:
                found = True
                break

        result = ""
        if found:
            result = "List contains value. Took {0} steps.".format(steps)
        else:
            result = "List doesn't contain value. Took {0} steps.".format(steps)
        return result

    def containsValueOrderedList(self, value, list):
        size = len(list)
        if size == 0:
            return False

        found = False
        steps = 0
        if value <= list[size-1]:
            starting = 0

            if value > list[size//2]:
                starting = size//2

            for i in range(starting, size):
                steps += 1
                if list[i] == value:
                    found = True
                    break

        result = ""
        if found:
            result = "List contains value. Took {0} steps.".format(steps)
        else:
            result = "List doesn't contain value. Took {0} steps.".format(steps)
        return result


numbers = []
for i in range(10000000):
    numbers.append(i)

search = SequentialSearch()
print(search.containsValue(924681,numbers))
numbers.sort()
print(search.containsValueOrderedList(924681,numbers))