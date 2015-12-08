class InsertionSort(object):
    def __init__(self):
        pass

    def sort(self, list):
        for i in range(1,len(list)):
            currentValue = list[i]
            position = i

            for j in range(i):
                if list[position-1] > currentValue:
                    list[position] = list[position-1]
                else:
                    break

                position -= 1

            list[position] = currentValue


    def sortAlternateMethod(self, list):
        for i in range(1, len(list)):
            currentValue = list[i]
            position = i

            while position > 0 and list[position-1] > currentValue:
                list[position] = list[position-1]
                position -= 1

            list[position] = currentValue