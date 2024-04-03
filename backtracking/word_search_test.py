from word_search import Solution


def test_exist():
    assert (
        Solution().exist(
            board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            word="ABCCED",
        )
        is True
    )
