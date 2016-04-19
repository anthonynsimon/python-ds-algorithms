class BubbleSort(object):

    def sort(self, data):
        if type(data) is not list or len(data) < 1:
            return

        done = False
        while not done:
            exchanges = 0
            for i in range(len(data)-1):
                if data[i] > data[i+1]:
                    temp = data[i]
                    data[i] = data[i + 1]
                    data[i + 1] = temp
                    exchanges += 1
            if exchanges == 0:
                done = True