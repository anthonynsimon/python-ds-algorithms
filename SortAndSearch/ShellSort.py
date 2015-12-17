class ShellSort(object):

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        gap = 1
        while gap < len(listToSort):
            gap = gap * 3 + 1

        while gap > 0:
            for iterationStartIndex in range(gap, len(listToSort)):
                value = listToSort[iterationStartIndex]
                currentIndex = iterationStartIndex
                while currentIndex - gap >= 0:
                    if listToSort[currentIndex - gap] > value:
                        listToSort[currentIndex] = listToSort[currentIndex - gap]
                    else:
                        break
                    currentIndex -= gap
                listToSort[currentIndex] = value
            gap = gap // 3