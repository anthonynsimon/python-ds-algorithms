class ShellSort(object):
    def __init__(self):
        pass

    def sort(self, list):
        gap = 1
        while gap < len(list):
            gap = gap * 3 + 1

        while gap > 0:
            for iterationStartIndex in range(gap, len(list)):
                value = list[iterationStartIndex]
                currentIndex = iterationStartIndex

                while currentIndex - gap >= 0:
                    if list[currentIndex - gap] > value:
                        list[currentIndex] = list[currentIndex - gap]
                    else:
                        break

                    currentIndex -= gap

                list[currentIndex] = value

            gap = gap // 3