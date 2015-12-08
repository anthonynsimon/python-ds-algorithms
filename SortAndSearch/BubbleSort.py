class BubbleSort(object):
    def __init__(self):
        pass

    def sort(self, list):
        done = False

        while not done:
            exchanges = 0

            for i in range(len(list)-1):
                if list[i] > list[i+1]:
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
                    exchanges += 1

            if exchanges == 0:
                done = True