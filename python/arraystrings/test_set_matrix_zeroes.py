import pytest
from .set_matrix_zeroes import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_matrix(solution):
    matrix = []
    solution.setZeroes(matrix)
    assert matrix == []


def test_single_element_zero(solution):
    matrix = [[0]]
    solution.setZeroes(matrix)
    assert matrix == [[0]]


def test_single_element_non_zero(solution):
    matrix = [[1]]
    solution.setZeroes(matrix)
    assert matrix == [[1]]


def test_2x2_matrix_with_zero(solution):
    matrix = [[1, 1], [1, 0]]
    solution.setZeroes(matrix)
    assert matrix == [[1, 0], [0, 0]]


def test_2x2_matrix_all_zeros(solution):
    matrix = [[0, 0], [0, 0]]
    solution.setZeroes(matrix)
    assert matrix == [[0, 0], [0, 0]]


def test_leetcode_example_1(solution):
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_leetcode_example_2(solution):
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


def test_multiple_zeros_in_same_row(solution):
    matrix = [[1, 0, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
    solution.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [1, 0, 1, 0], [1, 0, 1, 0]]


def test_multiple_zeros_in_same_column(solution):
    matrix = [[1, 1, 1], [0, 1, 1], [0, 1, 1]]
    solution.setZeroes(matrix)
    assert matrix == [[0, 1, 1], [0, 0, 0], [0, 0, 0]]


def test_large_matrix(solution):
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 0, 20],
        [21, 22, 23, 24, 25],
    ]
    solution.setZeroes(matrix)
    assert matrix == [
        [1, 0, 3, 0, 5],
        [0, 0, 0, 0, 0],
        [11, 0, 13, 0, 15],
        [0, 0, 0, 0, 0],
        [21, 0, 23, 0, 25],
    ]


def test_matrix_with_no_zeros(solution):
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.setZeroes(matrix)
    assert matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_rectangular_matrix(solution):
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12]]
    solution.setZeroes(matrix)
    assert matrix == [[1, 0, 3, 4], [0, 0, 0, 0], [9, 0, 11, 12]]
