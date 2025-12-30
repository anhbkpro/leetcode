import unittest

from bfs.maximum_employees_to_be_invited_to_a_meeting import Solution


class TestMaximumInvitations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case with a cycle of length 3."""
        favorite = [2, 2, 1, 2]
        expected = 3  # Employees 0, 1, and 2 can form a round table
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_example_2(self):
        """Test case with multiple two-person cycles."""
        favorite = [1, 2, 0]
        expected = 3  # Employees can form a cycle: 0 -> 1 -> 2 -> 0
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_example_3(self):
        """Test case with two-person cycle and additional invitees."""
        favorite = [3, 0, 1, 4, 1]
        expected = 4  # Two-person cycle between 1 and 2, plus their admirers
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_single_pair(self):
        """Test case with just two employees who favor each other."""
        favorite = [1, 0]
        expected = 2
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_long_chain(self):
        """Test case with a long chain leading to a two-person cycle."""
        favorite = [1, 2, 1]  # 0 -> 1 <-> 2
        expected = 3  # Two-person cycle (1,2) plus one admirer (0)
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_multiple_cycles(self):
        """Test case with multiple cycles of different lengths."""
        favorite = [1, 2, 3, 4, 5, 0]  # 6-person cycle
        expected = 6
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_two_cycles_with_branches(self):
        """Test case with two cycles and branches."""
        favorite = [1, 2, 1, 3, 3, 4, 5, 4]
        # Two-person cycle (1,2) with admirer (0)
        # Two-person cycle (4,5) with admirers (3,6,7)
        expected = (
            3  # Maximum is either a 3-person cycle or two-person cycle with one branch
        )
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_self_favorite(self):
        """Test case where an employee favors themselves."""
        favorite = [0]
        expected = 1
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_complex_case(self):
        """Test complex case with multiple components."""
        favorite = [3, 0, 1, 4, 1, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 13]
        # Contains:
        # - Multiple two-person cycles with branches
        # - Longer cycles
        # - Chain ending in a cycle
        expected = 4  # Maximum is either a cycle or two-person cycle with branches
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)

    def test_all_favor_one(self):
        """Test case where all employees favor one person."""
        favorite = [1, 1, 1, 1]
        expected = 1  # Only one person can be seated with their favorite
        self.assertEqual(self.solution.maximumInvitations(favorite), expected)


if __name__ == "__main__":
    unittest.main()
