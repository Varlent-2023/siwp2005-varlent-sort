import unittest
from sort.insertion_sort import InsertionSort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        array = [3, 6, 8, 10, 1, 2, 1]
        expected = [1, 1, 2, 3, 6, 8, 10]

        print("Original array:", array)
        sorted_array = InsertionSort.insertion_sort(array.copy())  # Use .copy() to avoid modifying the original array
        print("Sorted array:", sorted_array)

        self.assertEqual(sorted_array, expected)

if __name__ == "__main__":
    unittest.main()