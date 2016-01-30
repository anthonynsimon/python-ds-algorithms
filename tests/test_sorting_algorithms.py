import unittest
from lib.sort_search.bubble_sort import BubbleSort
from lib.sort_search.selection_sort import SelectionSort
from lib.sort_search.insertion_sort import InsertionSort
from lib.sort_search.shell_sort import ShellSort
from lib.sort_search.merge_sort import MergeSort
from lib.sort_search.quick_sort import QuickSort


class TestSortingAlgorithms(unittest.TestCase):

    def getUnsortedList(self):
        return [14,17,15,6,4,0,19,7,13,12,20,10,2,5,1,11,18,16,3,9,8]

    def getCorrectResult(self):
        correctResult = []
        for i in range(len(self.getUnsortedList())):
            correctResult.append(i)
        return correctResult

    def runTest(self, sortingAlgorithm):
        numbers = self.getUnsortedList()
        repeatedNumbers = [2,2,0,77,2]
        wrongInput = 57

        sortingAlgorithm.sort(numbers)
        sortingAlgorithm.sort(repeatedNumbers)
        sortingAlgorithm.sort(repeatedNumbers)

        self.assertEqual(numbers, self.getCorrectResult())
        self.assertEqual(repeatedNumbers, [0,2,2,2,77])
        self.assertEqual(wrongInput, 57)

    def testBubbleSort(self):
        self.runTest(BubbleSort())

    def testSelectionSort(self):
        self.runTest(SelectionSort())

    def testInsertionSort(self):
        self.runTest(InsertionSort())

    def testShellSort(self):
        self.runTest(ShellSort())

    def testMergeSort(self):
        self.runTest(MergeSort())

    def testQuickSort(self):
        self.runTest(QuickSort())