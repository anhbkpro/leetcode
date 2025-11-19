import pytest
from .type_of_triangle import Solution


@pytest.fixture
def solution():
    return Solution()


def test_equilateral_triangle(solution):
    nums = [2, 2, 2]
    assert solution.triangleType(nums) == "equilateral"


def test_isosceles_triangle_same_first_two(solution):
    nums = [2, 2, 3]
    assert solution.triangleType(nums) == "isosceles"


def test_isosceles_triangle_same_last_two(solution):
    nums = [2, 3, 3]
    assert solution.triangleType(nums) == "isosceles"


def test_scalene_triangle(solution):
    nums = [3, 4, 5]
    assert solution.triangleType(nums) == "scalene"


def test_invalid_triangle_sum_equals_third(solution):
    nums = [1, 2, 3]
    assert solution.triangleType(nums) == "none"


def test_invalid_triangle_sum_less_than_third(solution):
    nums = [1, 2, 4]
    assert solution.triangleType(nums) == "none"


def test_equilateral_triangle_large_numbers(solution):
    nums = [100, 100, 100]
    assert solution.triangleType(nums) == "equilateral"


def test_isosceles_triangle_large_numbers(solution):
    nums = [100, 100, 150]
    assert solution.triangleType(nums) == "isosceles"


def test_scalene_triangle_large_numbers(solution):
    nums = [100, 150, 200]
    assert solution.triangleType(nums) == "scalene"


def test_unsorted_input(solution):
    nums = [5, 3, 4]
    assert solution.triangleType(nums) == "scalene"


def test_leetcode_example_1(solution):
    nums = [3, 3, 3]
    assert solution.triangleType(nums) == "equilateral"


def test_leetcode_example_2(solution):
    nums = [3, 4, 5]
    assert solution.triangleType(nums) == "scalene"
