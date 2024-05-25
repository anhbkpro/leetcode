from backtracking.word_break_ii import Solution


def test_word_break():
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == [
        "cat sand dog",
        "cats and dog",
    ]
