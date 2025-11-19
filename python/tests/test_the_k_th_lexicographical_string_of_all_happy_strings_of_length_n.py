import pytest
from backtracking.the_k_th_lexicographical_string_of_all_happy_strings_of_length_n import (
    Solution,
)


@pytest.fixture
def solution():
    return Solution()


def test_example_1(solution):
    """Test with n=1, k=3: should return 'c'"""
    assert solution.getHappyString(n=1, k=3) == "c"


def test_example_2(solution):
    """Test with n=1, k=4: should return empty string as k exceeds possible combinations"""
    assert solution.getHappyString(n=1, k=4) == ""


def test_example_3(solution):
    """Test with n=3, k=9: should return 'cab'"""
    assert solution.getHappyString(n=3, k=9) == "cab"


def test_length_2_first_string(solution):
    """Test first string with length 2: should return 'ab'"""
    assert solution.getHappyString(n=2, k=1) == "ab"


def test_length_2_last_string(solution):
    """Test last string with length 2: should return 'cb'"""
    assert solution.getHappyString(n=2, k=6) == "cb"


def test_invalid_k(solution):
    """Test with k larger than possible combinations: should return empty string"""
    assert solution.getHappyString(n=2, k=7) == ""


def test_length_3_middle_string(solution):
    """Test middle string with length 3: should return 'bab'"""
    assert solution.getHappyString(n=3, k=5) == "bab"
