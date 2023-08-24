from lc_68_text_justification import Solution


def test_full_justify():
    assert Solution.fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    ) == [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ]
