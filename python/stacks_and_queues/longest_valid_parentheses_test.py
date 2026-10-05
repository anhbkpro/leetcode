from .longest_valid_parentheses import Solution


def test_longest_valid_parentheses_when_extra_open_paren_at_start() -> None:
    input_s: str = "(()"
    expected_length: int = 2

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length


def test_longest_valid_parentheses_when_unmatched_parens_on_both_ends() -> None:
    input_s: str = ")()())"
    expected_length: int = 4

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length


def test_longest_valid_parentheses_when_string_is_empty() -> None:
    input_s: str = ""
    expected_length: int = 0

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length


def test_longest_valid_parentheses_when_no_valid_pair_exists() -> None:
    input_s: str = ")))((("
    expected_length: int = 0

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length


def test_longest_valid_parentheses_when_whole_string_is_nested() -> None:
    input_s: str = "((()))"
    expected_length: int = 6

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length


def test_longest_valid_parentheses_when_adjacent_groups_join() -> None:
    input_s: str = "()(())"
    expected_length: int = 6

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length


def test_longest_valid_parentheses_when_unmatched_close_splits_groups() -> None:
    input_s: str = "()())()()()"
    expected_length: int = 6

    actual_length: int = Solution().longestValidParentheses(input_s)

    assert actual_length == expected_length
