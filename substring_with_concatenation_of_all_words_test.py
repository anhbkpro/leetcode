from substring_with_concatenation_of_all_words import Solution


def test_findSubstring():
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert (
        Solution().findSubstring(
            "wordgoodgoodgoodbestword", ["word", "good", "best", "word"]
        )
        == []
    )
    assert Solution().findSubstring(
        "barfoofoobarthefoobarman", ["bar", "foo", "the"]
    ) == [6, 9, 12]
