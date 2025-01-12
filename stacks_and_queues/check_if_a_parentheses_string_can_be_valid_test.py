import unittest
from .check_if_a_parentheses_string_can_be_valid import Solution


class TestParenthesesValidation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test the first example from the problem description"""
        self.assertTrue(self.solution.canBeValid("))()))", "010100"))

    def test_example_2(self):
        """Test the second example from the problem description"""
        self.assertTrue(self.solution.canBeValid("()()", "0000"))

    def test_example_3(self):
        """Test the third example from the problem description"""
        self.assertFalse(self.solution.canBeValid(")", "0"))

    def test_odd_length(self):
        """Test strings with odd length"""
        self.assertFalse(self.solution.canBeValid("())", "000"))
        self.assertFalse(self.solution.canBeValid("(", "0"))
        self.assertFalse(self.solution.canBeValid("(()", "111"))

    def test_all_unlocked(self):
        """Test cases where all positions are unlocked"""
        self.assertTrue(self.solution.canBeValid("((()))", "000000"))
        self.assertTrue(self.solution.canBeValid("))((", "0000"))
        self.assertTrue(self.solution.canBeValid(")(", "00"))

    def test_all_locked(self):
        """Test cases where all positions are locked"""
        self.assertTrue(self.solution.canBeValid("(())", "1111"))
        self.assertFalse(self.solution.canBeValid("))((", "1111"))
        self.assertFalse(self.solution.canBeValid(")(", "11"))

    def test_mixed_locks(self):
        """Test cases with mixed locked and unlocked positions"""
        self.assertFalse(self.solution.canBeValid("())(", "0011"))
        self.assertFalse(self.solution.canBeValid(")()(", "0101"))
        self.assertFalse(self.solution.canBeValid("))))", "1100"))

    def test_edge_cases(self):
        """Test edge cases"""
        # Minimum valid length (2)
        self.assertTrue(self.solution.canBeValid("()", "11"))
        self.assertTrue(self.solution.canBeValid(")(", "00"))

        # All same characters
        self.assertTrue(self.solution.canBeValid("((((", "0000"))
        self.assertTrue(self.solution.canBeValid("))))", "0000"))

        # Alternating patterns
        self.assertTrue(self.solution.canBeValid("()()()", "101010"))
        self.assertFalse(self.solution.canBeValid("())()(", "111111"))

    def test_complex_patterns(self):
        """Test more complex patterns"""
        self.assertTrue(self.solution.canBeValid("(())))()(())", "100001111011"))
        self.assertFalse(self.solution.canBeValid(")(()))()(())", "111111111111"))
        self.assertTrue(self.solution.canBeValid("((())())", "11110000"))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
