class SelectionSort(object):
    def __init__(self):
        pass

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        for iteration in range(len(listToSort)):
            indexForMax = 0
            iterationLength = len(listToSort) - iteration

            for position in range(iterationLength):
                if listToSort[position] > listToSort[indexForMax]:
                    indexForMax = position

            temp = listToSort[iterationLength - 1]
            listToSort[iterationLength - 1] = listToSort[indexForMax]
            listToSort[indexForMax] = temp