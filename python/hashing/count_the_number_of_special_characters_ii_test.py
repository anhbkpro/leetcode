import pytest
from .count_the_number_of_special_characters_ii import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "word, expected",
    [
        # Basic cases
        ("aaAbcBC", 3),  # a, b, c all qualify
        ("abc", 0),  # no uppercase at all
        ("ABC", 0),  # no lowercase at all
        ("aA", 1),  # single special char
        ("Aa", 0),  # uppercase before lowercase → invalid
        # Order violations
        ("aAbB", 2),  # both qualify
        ("AaBb", 0),  # both violated
        ("aABb", 1),  # 'a' qualifies, 'b' violated (B before b)
        # Duplicates
        ("aabAA", 1),  # last 'a' at idx 1, first 'A' at idx 3 → qualifies
        ("aAa", 0),  # last 'a' at idx 2, first 'A' at idx 1 → violated
        # Edge cases
        ("", 0),  # empty string
        ("a", 0),  # single lowercase
        ("A", 0),  # single uppercase
        ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 26),  # all 26 qualify
    ],
)
def test_count_special_chars(solution, word, expected):
    assert solution.count_special_chars(word) == expected
