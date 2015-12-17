# TODO:
# Write an iterative solution

class MergeSort(object):

    def sort(self, listToSort):
        if type(listToSort) is not list or len(listToSort) < 1:
            return

        listToSort[:] = self.sortWorker(listToSort)

    def sortWorker(self, list,):
        if len(list) == 1:
            return list

        middle = len(list)//2
        left = self.sortWorker(list[0:middle])
        right = self.sortWorker(list[middle:len(list)])

        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + self.merge(left[1:len(left)], right)
        return [right[0]] + self.merge(right[1:len(right)], left)


# numbers = [14,17,15,6,4,0,19,7,13,12,20,10,2,5,1,11,18,16,3,9,8]
# mergeSort = MergeSort()
# mergeSort.sort(numbers)
# print("result =", numbers)