class ShellSort(object):

    def sort(self, data):
        if type(data) is not list or len(data) < 1:
            return

        gap = 1
        while gap < len(data):
            gap = gap * 3 + 1

        while gap > 0:
            for iter_start_index in range(gap, len(data)):
                value = data[iter_start_index]
                current_index = iter_start_index
                while current_index - gap >= 0:
                    if data[current_index - gap] > value:
                        data[current_index] = data[current_index - gap]
                    else:
                        break
                    current_index -= gap
                data[current_index] = value
            gap //= 3
