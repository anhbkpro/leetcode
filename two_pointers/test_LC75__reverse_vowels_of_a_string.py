import pytest
from two_pointers.LC75__reverse_vowels_of_a_string import Solution


@pytest.mark.parametrize(
    "input_s, expected_output",
    [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
        ("", ""),
        ("bcd", "bcd"),
        ("aeiou", "uoiea"),
        ("AEIOU", "UOIEA"),
        ("racecar", "racecar"),
        ("x", "x"),
        ("why", "why"),
        ("banana", "banana"),
        ("AaEeIiOoUu", "uUoOiIeEaA"),
    ],
)
def test_reverse_vowels(input_s, expected_output):
    solution = Solution()
    actual_output = solution.reverseVowels(input_s)
    assert actual_output == expected_output
