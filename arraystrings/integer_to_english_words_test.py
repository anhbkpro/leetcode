from .integer_to_english_words import Solution


def test_integer_to_english_words():
    assert Solution().numberToWords(123) == "One Hundred Twenty Three"
    assert Solution().numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"
    assert (
        Solution().numberToWords(1234567)
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )
