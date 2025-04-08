import pytest
from .put_marbles_in_bags import Solution


class TestPutMarbles:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        weights = [1, 3, 5, 1]
        k = 2
        assert solution.putMarbles(weights, k) == 4

    def test_example2(self, solution):
        weights = [1, 3]
        k = 2
        assert solution.putMarbles(weights, k) == 0

    def test_single_bag(self, solution):
        weights = [1, 2, 3, 4, 5]
        k = 1
        assert solution.putMarbles(weights, k) == 0

    def test_two_bags(self, solution):
        weights = [1, 2, 3, 4]
        k = 2
        assert solution.putMarbles(weights, k) == 4

    def test_all_same_weights(self, solution):
        weights = [1, 1, 1, 1, 1]
        k = 3
        assert solution.putMarbles(weights, k) == 0

    def test_increasing_weights(self, solution):
        weights = [1, 2, 3, 4, 5]
        k = 3
        assert solution.putMarbles(weights, k) == 8

    def test_decreasing_weights(self, solution):
        weights = [5, 4, 3, 2, 1]
        k = 3
        assert solution.putMarbles(weights, k) == 8

    def test_minimum_k(self, solution):
        weights = [1, 2, 3, 4, 5]
        k = 1
        assert solution.putMarbles(weights, k) == 0

    def test_maximum_k(self, solution):
        weights = [1, 2, 3, 4, 5]
        k = 5
        assert solution.putMarbles(weights, k) == 0

    def test_large_weights(self, solution):
        weights = [1000, 2000, 3000, 4000, 5000]
        k = 3
        assert solution.putMarbles(weights, k) == 8000

    def test_alternating_weights(self, solution):
        weights = [1, 10, 1, 10, 1, 10]
        k = 3
        assert solution.putMarbles(weights, k) == 0
