class InsertionSort(object):

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        for i in range(1, len(listToSort)):
            currentValue = listToSort[i]
            position = i
            for j in range(i):
                if listToSort[position-1] > currentValue:
                    listToSort[position] = listToSort[position - 1]
                else:
                    break
                position -= 1
            listToSort[position] = currentValue

    def sortAlternateMethod(self, list):
        for i in range(1, len(list)):
            currentValue = list[i]
            position = i
            while position > 0 and list[position-1] > currentValue:
                list[position] = list[position-1]
                position -= 1
            list[position] = currentValue