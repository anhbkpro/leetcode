import pytest

from .LC75__reverse_words_in_a_string import Solution


@pytest.fixture
def solution():
    return Solution()


def test_empty_string(solution):
    s = ""
    assert solution.reverseWords(s) == ""


def test_single_word(solution):
    s = "hello"
    assert solution.reverseWords(s) == "hello"


def test_two_words(solution):
    s = "hello world"
    assert solution.reverseWords(s) == "world hello"


def test_leetcode_example_1(solution):
    s = "the sky is blue"
    assert solution.reverseWords(s) == "blue is sky the"


def test_leetcode_example_2(solution):
    s = "  hello world  "
    assert solution.reverseWords(s) == "world hello"


def test_leetcode_example_3(solution):
    s = "a good   example"
    assert solution.reverseWords(s) == "example good a"


def test_multiple_spaces_between_words(solution):
    s = "hello    world"
    assert solution.reverseWords(s) == "world hello"


def test_leading_and_trailing_spaces(solution):
    s = "   hello   world   "
    assert solution.reverseWords(s) == "world hello"


def test_single_character_words(solution):
    s = "a b c d"
    assert solution.reverseWords(s) == "d c b a"


def test_long_sentence(solution):
    s = "the quick brown fox jumps over the lazy dog"
    assert solution.reverseWords(s) == "dog lazy the over jumps fox brown quick the"


def test_words_with_special_characters(solution):
    s = "hello! world@ python#"
    assert solution.reverseWords(s) == "python# world@ hello!"


def test_words_with_numbers(solution):
    s = "hello 123 world 456"
    assert solution.reverseWords(s) == "456 world 123 hello"


def test_mixed_case_words(solution):
    s = "Hello World PYTHON"
    assert solution.reverseWords(s) == "PYTHON World Hello"


def test_repeated_words(solution):
    s = "hello hello world world"
    assert solution.reverseWords(s) == "world world hello hello"
