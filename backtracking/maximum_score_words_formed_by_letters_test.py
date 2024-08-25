from backtracking.maximum_score_words_formed_by_letters import Solution


def test_max_score_words():
    assert (
        Solution().maxScoreWords(
            words=["dog", "cat", "dad", "good"],
            letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
            score=[
                1,
                0,
                9,
                5,
                0,
                0,
                3,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        )
        == 23
    )
