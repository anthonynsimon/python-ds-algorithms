class SelectionSort(object):

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        for iteration in range(len(listToSort)):
            indexForMax = 0
            iterationLength = len(listToSort) - iteration
            for position in range(iterationLength):
                if listToSort[position] > listToSort[indexForMax]:
                    indexForMax = position
            self.swapContents(iterationLength-1, indexForMax, listToSort)

    def swapContents(self, indexA, indexB, list):
        list[indexA], list[indexB] = list[indexB], list[indexA]