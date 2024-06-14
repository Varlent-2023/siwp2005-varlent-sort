import unittest
from sort.quick_sort import QuickSort

class TestQuickSort(unittest.TestCase):
    def test_quicksort(self):
        array = [3, 6, 8, 10, 1, 2, 1]
        expected = [1, 1, 2, 3, 6, 8, 10]

        print("Original array:", array)
        sorted_array = QuickSort.quicksort(array.copy())
        print("Sorted array:", sorted_array)

        self.assertEqual(sorted_array, expected)

if __name__ == "__main__":
    unittest.main()