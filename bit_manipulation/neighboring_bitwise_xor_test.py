import unittest
from .neighboring_bitwise_xor import Solution


class TestValidBinaryArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case from Example 1: [1,1,0]"""
        derived = [1, 1, 0]
        self.assertTrue(self.solution.doesValidArrayExist(derived))

    def test_example_2(self):
        """Test case from Example 2: [1,1]"""
        derived = [1, 1]
        self.assertTrue(self.solution.doesValidArrayExist(derived))

    def test_example_3(self):
        """Test case from Example 3: [1,0]"""
        derived = [1, 0]
        self.assertFalse(self.solution.doesValidArrayExist(derived))

    def test_single_element(self):
        """Test array with single element"""
        self.assertTrue(self.solution.doesValidArrayExist([0]))
        self.assertFalse(self.solution.doesValidArrayExist([1]))

    def test_all_zeros(self):
        """Test array with all zeros"""
        self.assertTrue(self.solution.doesValidArrayExist([0, 0, 0]))
        self.assertTrue(self.solution.doesValidArrayExist([0, 0, 0, 0]))

    def test_all_ones(self):
        """Test array with all ones"""
        self.assertFalse(self.solution.doesValidArrayExist([1, 1, 1]))
        self.assertTrue(self.solution.doesValidArrayExist([1, 1, 1, 1]))

    def test_alternating_values(self):
        """Test array with alternating 0s and 1s"""
        self.assertTrue(self.solution.doesValidArrayExist([1, 1, 1, 1]))
        self.assertFalse(self.solution.doesValidArrayExist([1, 1, 1]))

    def test_large_array(self):
        """Test larger array"""
        derived = [1, 0, 1, 0, 1, 0, 1, 0]  # 8 elements
        self.assertTrue(self.solution.doesValidArrayExist(derived))

    def test_verify_original_array(self):
        """Verify if we can construct a valid original array for a true case"""
        derived = [1, 1, 0]  # From Example 1
        result = self.solution.doesValidArrayExist(derived)

        if result:
            # Verify one possible original array [0,1,0]
            original = [0, 1, 0]
            n = len(original)
            constructed_derived = []

            for i in range(n):
                if i == n - 1:
                    constructed_derived.append(original[i] ^ original[0])
                else:
                    constructed_derived.append(original[i] ^ original[i + 1])

            self.assertEqual(derived, constructed_derived)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
