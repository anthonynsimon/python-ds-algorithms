class SequentialSearch(object):

    def contains_value(self, value, data):
        if len(data) == 0:
            return False

        found = False
        steps = 0
        for i in range(len(data)):
            steps += 1
            if data[i] == value:
                found = True
                break

        result = ""
        if found:
            result = "List contains value. Took {0} steps.".format(steps)
        else:
            result = "List doesn't contain value. Took {0} steps.".format(steps)
        return result

    def contains_value_ordered_list(self, value, data):
        size = len(data)
        if size == 0:
            return False

        found = False
        steps = 0
        if value <= data[size-1]:
            starting = 0

            if value > data[size//2]:
                starting = size//2

            for i in range(starting, size):
                steps += 1
                if data[i] == value:
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
print(search.contains_value(924681, numbers))
numbers.sort()
print(search.contains_value_ordered_list(924681, numbers))