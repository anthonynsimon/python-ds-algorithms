class BubbleSort(object):

    def __init__(self):
        pass

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        done = False
        while not done:
            exchanges = 0
            for i in range(len(listToSort)-1):
                if listToSort[i] > listToSort[i+1]:
                    temp = listToSort[i]
                    listToSort[i] = listToSort[i + 1]
                    listToSort[i + 1] = temp
                    exchanges += 1
            if exchanges == 0:
                done = True