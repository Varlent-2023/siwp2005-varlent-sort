import unittest
from sort.bubble_sort import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        array = [15, 3, 6, 12, 8, 10, 7, 1, 2, 1]
        expected = [1, 1, 2, 3, 6, 7, 8, 10, 12, 15]

        print("Original array:", array)
        sorted_array = BubbleSort.bubble_sort(array.copy())
        print("Sorted array:", sorted_array)

        self.assertEqual(sorted_array, expected)

if __name__ == "__main__":
    unittest.main()
