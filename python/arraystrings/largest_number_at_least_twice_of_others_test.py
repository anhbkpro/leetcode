import unittest

from .largest_number_at_least_twice_of_others import Solution


class TestDominantIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from Example 1: [3,6,1,0]"""
        nums = [3, 6, 1, 0]
        self.assertEqual(self.solution.dominantIndex(nums), 1)

    def test_example_2(self):
        """Test case from Example 2: [1,2,3,4]"""
        nums = [1, 2, 3, 4]
        self.assertEqual(self.solution.dominantIndex(nums), -1)

    def test_single_element(self):
        """Test array with a single element"""
        nums = [5]
        self.assertEqual(self.solution.dominantIndex(nums), 0)

    def test_two_elements_dominant(self):
        """Test array with two elements where first is dominant"""
        nums = [10, 4]
        self.assertEqual(self.solution.dominantIndex(nums), 0)

    def test_two_elements_not_dominant(self):
        """Test array with two elements where first is not dominant"""
        nums = [5, 3]
        self.assertEqual(self.solution.dominantIndex(nums), -1)

    def test_zero_included(self):
        """Test array including zero"""
        nums = [0, 5, 0, 0]
        self.assertEqual(self.solution.dominantIndex(nums), 1)

    def test_largest_at_beginning(self):
        """Test array with largest number at the beginning"""
        nums = [10, 3, 2, 4]
        self.assertEqual(self.solution.dominantIndex(nums), 0)

    def test_largest_at_end(self):
        """Test array with largest number at the end"""
        nums = [1, 2, 3, 8]
        self.assertEqual(self.solution.dominantIndex(nums), 3)

    def test_barely_not_dominant(self):
        """Test case where largest is just shy of being twice others"""
        nums = [5, 3]  # 5 is not >= 2*3
        self.assertEqual(self.solution.dominantIndex(nums), -1)

    def test_barely_dominant(self):
        """Test case where largest is exactly twice others"""
        nums = [6, 3]  # 6 is exactly 2*3
        self.assertEqual(self.solution.dominantIndex(nums), 0)

    def test_all_same_except_largest(self):
        """Test array where all elements except largest are the same"""
        nums = [2, 2, 5, 2]
        self.assertEqual(self.solution.dominantIndex(nums), 2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
