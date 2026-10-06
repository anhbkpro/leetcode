from .minimum_add_to_make_parentheses_valid import Solution


def test_min_add_to_make_valid_when_extra_close_paren() -> None:
    input_s: str = "())"
    expected_additions: int = 1

    actual_additions: int = Solution().minAddToMakeValid(input_s)

    assert actual_additions == expected_additions


def test_min_add_to_make_valid_when_only_open_parens() -> None:
    input_s: str = "((("
    expected_additions: int = 3

    actual_additions: int = Solution().minAddToMakeValid(input_s)

    assert actual_additions == expected_additions


def test_min_add_to_make_valid_when_already_valid() -> None:
    input_s: str = "()"
    expected_additions: int = 0

    actual_additions: int = Solution().minAddToMakeValid(input_s)

    assert actual_additions == expected_additions


def test_min_add_to_make_valid_when_string_is_empty() -> None:
    input_s: str = ""
    expected_additions: int = 0

    actual_additions: int = Solution().minAddToMakeValid(input_s)

    assert actual_additions == expected_additions


def test_min_add_to_make_valid_when_close_parens_come_first() -> None:
    input_s: str = ")))((("
    expected_additions: int = 6

    actual_additions: int = Solution().minAddToMakeValid(input_s)

    assert actual_additions == expected_additions


def test_min_add_to_make_valid_when_unmatched_on_both_sides() -> None:
    input_s: str = "()))(("
    expected_additions: int = 4

    actual_additions: int = Solution().minAddToMakeValid(input_s)

    assert actual_additions == expected_additions
