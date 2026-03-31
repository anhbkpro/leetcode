import pytest

from arraystrings.lexicographically_smallest_generated_string import Solution


@pytest.fixture
def generate_solution() -> Solution:
    return Solution()


def test_generate_string_single_true_constraint(
    generate_solution: Solution,
) -> None:
    # Arrange
    input_str1: str = "T"
    input_str2: str = "abc"
    expected_result: str = "abc"
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_overlapping_true_constraints_agree(
    generate_solution: Solution,
) -> None:
    # Arrange — two windows of length 3 over "aaa" share consistently
    input_str1: str = "TT"
    input_str2: str = "aaa"
    expected_result: str = "aaaa"
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_returns_empty_on_conflicting_true_constraints(
    generate_solution: Solution,
) -> None:
    # Arrange — overlapping T windows require incompatible characters
    input_str1: str = "TT"
    input_str2: str = "ab"
    expected_result: str = ""
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_false_only_breaks_equality_at_rightmost_free_position(
    generate_solution: Solution,
) -> None:
    # Arrange — default "aaa" equals str2; bump rightmost unfixed index to "b"
    input_str1: str = "F"
    input_str2: str = "aaa"
    expected_result: str = "aab"
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_false_skips_when_substring_already_differs(
    generate_solution: Solution,
) -> None:
    # Arrange — defaults "aaa" already differ from "abc" at position 1
    input_str1: str = "F"
    input_str2: str = "abc"
    expected_result: str = "aaa"
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_returns_empty_when_false_window_is_all_fixed(
    generate_solution: Solution,
) -> None:
    # Arrange — all T first fix the F window; no free index left to break equality
    input_str1: str = "TFT"
    input_str2: str = "aa"
    expected_result: str = ""
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_mixed_pattern_after_all_true_then_false(
    generate_solution: Solution,
) -> None:
    # Arrange — four T windows for m=1 fix leading a's; last F bumps next char to b
    input_str1: str = "TTTTF"
    input_str2: str = "a"
    expected_result: str = "aaaab"
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result


def test_generate_string_minimum_length_true_constraint(
    generate_solution: Solution,
) -> None:
    # Arrange
    input_str1: str = "T"
    input_str2: str = "a"
    expected_result: str = "a"
    # Act
    actual_result: str = generate_solution.generateString(input_str1, input_str2)
    # Assert
    assert actual_result == expected_result
