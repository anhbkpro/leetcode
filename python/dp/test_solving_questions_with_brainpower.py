import pytest

from .solving_questions_with_brainpower import Solution


class TestSolvingQuestionsWithBrainpower:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        questions = [[3, 2], [4, 3], [4, 4], [2, 5]]
        assert solution.mostPoints(questions) == 5

    def test_example2(self, solution):
        questions = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        assert solution.mostPoints(questions) == 7

    def test_single_question(self, solution):
        questions = [[1, 1]]
        assert solution.mostPoints(questions) == 1

    def test_two_questions(self, solution):
        questions = [[1, 1], [2, 1]]
        assert solution.mostPoints(questions) == 2

    def test_skip_all(self, solution):
        questions = [[1, 2], [2, 2], [3, 2]]
        assert solution.mostPoints(questions) == 3

    def test_solve_all(self, solution):
        questions = [[1, 0], [2, 0], [3, 0]]
        assert solution.mostPoints(questions) == 6

    def test_mixed_strategy(self, solution):
        questions = [[1, 2], [2, 1], [3, 2], [4, 1]]
        assert solution.mostPoints(questions) == 6

    def test_large_values(self, solution):
        questions = [[1000, 2], [2000, 1], [3000, 2], [4000, 1]]
        assert solution.mostPoints(questions) == 6000

    def test_zero_points(self, solution):
        questions = [[0, 1], [0, 2], [0, 3]]
        assert solution.mostPoints(questions) == 0

    def test_zero_brainpower(self, solution):
        questions = [[1, 0], [2, 0], [3, 0]]
        assert solution.mostPoints(questions) == 6

    def test_skip_last(self, solution):
        questions = [[1, 1], [2, 2], [3, 1]]
        assert solution.mostPoints(questions) == 4

    def test_skip_first(self, solution):
        questions = [[1, 2], [2, 1], [3, 1]]
        assert solution.mostPoints(questions) == 3
