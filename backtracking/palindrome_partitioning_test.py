from backtracking.palindrome_partitioning import Solution


def test_partition():
    assert Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert Solution().partition("a") == [["a"]]
