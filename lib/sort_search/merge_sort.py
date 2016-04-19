class MergeSort(object):

    def sort(self, data):
        if type(data) is not list or len(data) < 1:
            return

        data[:] = self.__sort_helper(data)

    def __sort_helper(self, list, ):
        if len(list) == 1:
            return list

        middle = len(list)//2
        left = self.__sort_helper(list[0:middle])
        right = self.__sort_helper(list[middle:len(list)])

        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + self.merge(left[1:len(left)], right)
        return [right[0]] + self.merge(right[1:len(right)], left)
