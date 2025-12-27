import pytest
from heaps.maximize_happiness_of_selected_children import Solution


class TestMaximizeHappinessOfSelectedChildren:
    """Test suite for maximumHappinessSum function."""

    def setup_method(self):
        """Initialize solution instance for each test."""
        self.solution = Solution()

    def test_basic_case_with_mixed_values(self):
        """Test basic case with mixed happiness values."""
        assert self.solution.maximumHappinessSum(happiness=[1, 2, 3], k=2) == 4

    def test_all_identical_happiness_values(self):
        """Test case where all happiness values are the same."""
        assert self.solution.maximumHappinessSum(happiness=[1, 1, 1, 1], k=2) == 1

    def test_single_selection(self):
        """Test case where we select only one child (k=1)."""
        assert self.solution.maximumHappinessSum(happiness=[2, 3, 4, 5], k=1) == 5

    def test_select_all_children(self):
        """Test case where k equals the number of children."""
        result = self.solution.maximumHappinessSum(happiness=[1, 2, 3], k=3)
        # happiness values: [3, 2, 1], turns: [0, 1, 2]
        # selections: 3-0 + 2-1 + max(1-2, 0) = 3 + 1 + 0 = 4
        assert result == 4

    def test_single_child(self):
        """Test case with a single child."""
        assert self.solution.maximumHappinessSum(happiness=[10], k=1) == 10

    def test_k_larger_than_children_count(self):
        """Test case where k is larger than the number of children."""
        # Should select all available children: 10-0 + 5-1 = 10 + 4 = 14
        assert self.solution.maximumHappinessSum(happiness=[5, 10], k=5) == 14

    def test_large_happiness_values(self):
        """Test case with large happiness values."""
        # 300-0 + 200-1 = 300 + 199 = 499
        assert self.solution.maximumHappinessSum(happiness=[100, 200, 300], k=2) == 499

    def test_decreasing_happiness_turns_zero(self):
        """Test case where happiness decreases to zero due to turns."""
        # happiness=[1, 2], k=3, but only 2 children available
        # selections: 2-0 + 1-1 = 2 + 0 = 2
        assert self.solution.maximumHappinessSum(happiness=[1, 2], k=3) == 2

    def test_zero_result(self):
        """Test case that results in zero total happiness."""
        assert self.solution.maximumHappinessSum(happiness=[0, 0, 0], k=2) == 0

    def test_many_children_select_few(self):
        """Test case with many children but selecting only a few."""
        assert self.solution.maximumHappinessSum(
            happiness=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=3
        ) == 24

    @pytest.mark.parametrize(
        "happiness,k,expected",
        [
            ([5], 1, 5),                           # 5-0 = 5
            ([1, 2], 1, 2),                        # 2-0 = 2
            ([10, 20, 30], 2, 49),                 # 30-0 + 20-1 = 49
            ([1, 1, 1], 3, 1),                     # 1-0 + 1-1 + max(1-2, 0) = 1
            (list(range(1, 11)), 5, 30),           # 10-0 + 9-1 + 8-2 + 7-3 + 6-4 = 30
        ],
    )
    def test_parametrized_cases(self, happiness, k, expected):
        """Parametrized test for various input combinations."""
        assert self.solution.maximumHappinessSum(happiness=happiness, k=k) == expected
