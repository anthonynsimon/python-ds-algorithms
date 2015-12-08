class SelectionSort(object):
    def __init__(self):
        pass

    def sort(self, list):
        for iteration in range(len(list)):
            indexForMax = 0
            iterationLength = len(list) - iteration

            for position in range(iterationLength):
                if list[position] > list[indexForMax]:
                    indexForMax = position

            temp = list[iterationLength-1]
            list[iterationLength-1] = list[indexForMax]
            list[indexForMax] = temp