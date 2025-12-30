import unittest

from .minimum_deletions_to_make_string_k_special import Solution


class TestMinimumDeletions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        """Test with empty string"""
        self.assertEqual(self.solution.minimumDeletions("", 1), 0)

    def test_single_character(self):
        """Test with single character"""
        self.assertEqual(self.solution.minimumDeletions("a", 1), 0)
        self.assertEqual(self.solution.minimumDeletions("a", 0), 0)

    def test_all_same_characters(self):
        """Test with all same characters"""
        self.assertEqual(self.solution.minimumDeletions("aaaa", 1), 0)
        self.assertEqual(self.solution.minimumDeletions("aaaa", 0), 0)

    def test_two_different_characters(self):
        """Test with two different characters"""
        # "ab" - frequencies are 1,1 - difference is 0, so no deletions needed
        self.assertEqual(self.solution.minimumDeletions("ab", 0), 0)
        self.assertEqual(self.solution.minimumDeletions("ab", 1), 0)

        # "aab" - frequencies are 2,1 - difference is 1
        self.assertEqual(
            self.solution.minimumDeletions("aab", 0), 1
        )  # delete one 'a' or one 'b'
        self.assertEqual(
            self.solution.minimumDeletions("aab", 1), 0
        )  # difference <= 1, so no deletions

    def test_three_different_characters(self):
        """Test with three different characters"""
        # "abc" - frequencies are 1,1,1 - no deletions needed
        self.assertEqual(self.solution.minimumDeletions("abc", 0), 0)

        # "aabbc" - frequencies are 2,2,1 - difference is 1
        self.assertEqual(
            self.solution.minimumDeletions("aabbc", 0), 1
        )  # delete one 'a' or one 'b'
        self.assertEqual(
            self.solution.minimumDeletions("aabbc", 1), 0
        )  # difference <= 1

    def test_large_frequency_differences(self):
        """Test with large frequency differences"""
        # "aaaaab" - frequencies are 5,1 - difference is 4
        self.assertEqual(
            self.solution.minimumDeletions("aaaaab", 0), 1
        )  # delete 4 'a's or 1 'b'
        self.assertEqual(
            self.solution.minimumDeletions("aaaaab", 1), 1
        )  # delete 3 'a's to make diff <= 1
        self.assertEqual(
            self.solution.minimumDeletions("aaaaab", 2), 1
        )  # delete 2 'a's to make diff <= 2
        self.assertEqual(
            self.solution.minimumDeletions("aaaaab", 3), 1
        )  # delete 1 'a' to make diff <= 3
        self.assertEqual(
            self.solution.minimumDeletions("aaaaab", 4), 0
        )  # difference <= 4, no deletions

    def test_complex_case(self):
        """Test with more complex case"""
        # "aabbbcccc" - frequencies are 2,3,4 - differences are 1,2,1
        self.assertEqual(
            self.solution.minimumDeletions("aabbbcccc", 0), 3
        )  # delete 2 'c's to make all equal
        self.assertEqual(
            self.solution.minimumDeletions("aabbbcccc", 1), 1
        )  # delete 1 'c' to make diff <= 1
        self.assertEqual(
            self.solution.minimumDeletions("aabbbcccc", 2), 0
        )  # difference <= 2, no deletions

    def test_edge_case_k_zero(self):
        """Test edge case where k=0 (all frequencies must be equal)"""
        self.assertEqual(self.solution.minimumDeletions("aab", 0), 1)
        self.assertEqual(self.solution.minimumDeletions("aabb", 0), 0)
        self.assertEqual(self.solution.minimumDeletions("aabbc", 0), 1)

    def test_large_k(self):
        """Test with large k values"""
        word = "aabbbcccc"
        # With large k, no deletions should be needed
        self.assertEqual(self.solution.minimumDeletions(word, 10), 0)
        self.assertEqual(self.solution.minimumDeletions(word, 100), 0)

    def test_special_characters(self):
        """Test with special characters and numbers"""
        self.assertEqual(
            self.solution.minimumDeletions("a1a1", 0), 0
        )  # frequencies are 2,2
        self.assertEqual(
            self.solution.minimumDeletions("a1a1a", 0), 1
        )  # frequencies are 3,2
        self.assertEqual(
            self.solution.minimumDeletions("a1a1a", 1), 0
        )  # difference <= 1

    def test_leetcode_example(self):
        """Test with LeetCode example cases"""
        # Example 1: word = "aabcaba", k = 0
        # Frequencies: a=4, b=2, c=1
        # To make all equal (k=0), we need to delete 3 'a's or delete 1 'b' and 2 'a's
        # Minimum is 3 deletions
        self.assertEqual(self.solution.minimumDeletions("aabcaba", 0), 3)

        # Example 2: word = "dabdcbdcdcd", k = 2
        # Frequencies: d=5, a=1, b=2, c=3
        # With k=2, we can have max difference of 2
        # Current max difference is 4 (between d=5 and a=1)
        # We need to delete 2 'd's to make difference <= 2
        self.assertEqual(self.solution.minimumDeletions("dabdcbdcdcd", 2), 2)

        # Example 3: word = "aaabaaa", k = 2
        # Frequencies: a=6, b=1
        # With k=2, max difference can be 2
        # Current difference is 5, so we need to delete 3 'a's
        self.assertEqual(self.solution.minimumDeletions("aaabaaa", 2), 1)
