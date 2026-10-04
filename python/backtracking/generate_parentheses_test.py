from typing import List

from .generate_parentheses import Solution


def test_generate_parenthesis_when_n_is_one() -> None:
    input_n: int = 1
    expected_combinations: List[str] = ["()"]

    actual_combinations: List[str] = Solution().generateParenthesis(input_n)

    assert actual_combinations == expected_combinations


def test_generate_parenthesis_when_n_is_two() -> None:
    input_n: int = 2
    expected_combinations: List[str] = ["(())", "()()"]

    actual_combinations: List[str] = Solution().generateParenthesis(input_n)

    assert actual_combinations == expected_combinations


def test_generate_parenthesis_when_n_is_three() -> None:
    input_n: int = 3
    expected_combinations: List[str] = [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]

    actual_combinations: List[str] = Solution().generateParenthesis(input_n)

    assert actual_combinations == expected_combinations


def test_generate_parenthesis_count_matches_catalan_number() -> None:
    input_n: int = 5
    expected_count: int = 42

    actual_count: int = len(Solution().generateParenthesis(input_n))

    assert actual_count == expected_count


def test_generate_parenthesis_produces_unique_balanced_strings() -> None:
    input_n: int = 4

    actual_combinations: List[str] = Solution().generateParenthesis(input_n)

    assert len(actual_combinations) == len(set(actual_combinations))
    assert all(is_balanced(combination) for combination in actual_combinations)


def is_balanced(combination: str) -> bool:
    depth: int = 0
    for char in combination:
        depth += 1 if char == "(" else -1
        if depth < 0:
            return False
    return depth == 0
