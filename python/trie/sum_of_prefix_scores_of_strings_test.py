from .sum_of_prefix_scores_of_strings import Solution


def test_sum_prefix_scores():
    assert Solution().sumPrefixScores(words=["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
