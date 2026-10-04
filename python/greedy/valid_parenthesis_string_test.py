from .valid_parenthesis_string import Solution


def test_check_valid_string_when_simple_pair() -> None:
    input_s: str = "()"

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is True


def test_check_valid_string_when_star_is_empty() -> None:
    input_s: str = "(*)"

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is True


def test_check_valid_string_when_star_is_close_paren() -> None:
    input_s: str = "(*))"

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is True


def test_check_valid_string_when_string_is_empty() -> None:
    input_s: str = ""

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is True


def test_check_valid_string_when_only_stars() -> None:
    input_s: str = "***"

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is True


def test_check_valid_string_when_close_paren_comes_first() -> None:
    input_s: str = ")("

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is False


def test_check_valid_string_when_too_many_open_parens() -> None:
    input_s: str = "(((*)"

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is False


def test_check_valid_string_when_star_before_open_paren_cannot_close_it() -> None:
    input_s: str = "*("

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is False


def test_check_valid_string_when_stars_balance_complex_string() -> None:
    input_s: str = "(*()**)*"

    actual_is_valid: bool = Solution().checkValidString(input_s)

    assert actual_is_valid is True
