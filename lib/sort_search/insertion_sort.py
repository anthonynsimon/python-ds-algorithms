class InsertionSort(object):

    def sort(self, data):
        if type(data) is not list or len(data) < 1:
            return

        for i in range(1, len(data)):
            current = data[i]
            position = i
            for j in range(i):
                if data[position-1] > current:
                    data[position] = data[position - 1]
                else:
                    break
                position -= 1
            data[position] = current

    def sort_alternative(self, list):
        for i in range(1, len(list)):
            current = list[i]
            position = i
            while position > 0 and list[position-1] > current:
                list[position] = list[position-1]
                position -= 1
            list[position] = current