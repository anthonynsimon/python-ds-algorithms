class SelectionSort(object):

    def sort(self, data):
        if type(data) is not list or len(data) < 1:
            return

        for iteration in range(len(data)):
            index_max = 0 # Index for the max value
            iter_length = len(data) - iteration
            for position in range(iter_length):
                if data[position] > data[index_max]:
                    index_max = position
            self.__swap_contents(iter_length - 1, index_max, data)

    def __swap_contents(self, a, b, data):
        data[a], data[b] = data[b], data[a]