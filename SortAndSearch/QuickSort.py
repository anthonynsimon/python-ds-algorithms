# TODO:
# Pick the pivot from the median of first, middle and last elements

class QuickSort(object):
    def __init__(self):
        pass

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        self.sortWorker(listToSort, 0, len(listToSort) - 1)

    def sortWorker(self, listToSort, first, last):
        if first >= last:
            return

        pivot = last
        left = first
        right = last

        while left <= right:
            while listToSort[left] < listToSort[pivot]:
                left += 1
            while listToSort[right] > listToSort[pivot]:
                right -= 1

            if left <= right:
                listToSort[left], listToSort[right] = listToSort[right], listToSort[left]
                right -= 1
                left += 1

        self.sortWorker(listToSort, first, right)
        self.sortWorker(listToSort, left, last)


# numbers = [14,17,15,6,4,0,19,7,13,12,20,10,2,5,1,11,18,16,8,9,3,]
# quickSort = QuickSort()
# quickSort.sort(numbers)
# print("result =", numbers)
