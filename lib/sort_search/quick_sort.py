# TODO:
# Pick the pivot from the median of first, middle and last elements

class QuickSort(object):

    def sort(self, data):
        if type(data) is not list or len(data) < 1:
            return

        self.__sort_helper(data, 0, len(data) - 1)

    def __sort_helper(self, data, first, last):
        if first >= last:
            return

        pivot = last
        left = first
        right = last

        while left <= right:
            while data[left] < data[pivot]:
                left += 1
            while data[right] > data[pivot]:
                right -= 1
            if left <= right:
                data[left], data[right] = data[right], data[left]
                right -= 1
                left += 1

        self.__sort_helper(data, first, right)
        self.__sort_helper(data, left, last)
