import unittest
from sliding_windows.count_of_substrings_containing_every_vowel_and_k_consonants_ii import Solution

class TestCountOfSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.countOfSubstrings("aeioqq", 1), 0)

    def test_no_vowels(self):
        self.assertEqual(self.solution.countOfSubstrings("aeiou", 0), 1)

    def test_no_consonants(self):
        self.assertEqual(self.solution.countOfSubstrings("ieaouqqieaouqq", 1), 3)

if __name__ == "__main__":
    unittest.main()
