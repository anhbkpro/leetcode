from lc_1704_determine_if_string_halves_are_alike import Solution


def test_halves_are_alike():
    assert Solution().halvesAreAlike("book") is True
    assert Solution().halvesAreAlike("textbook") is False
