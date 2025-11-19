from .maximum_repeating_substring import Solution


def test_max_repeating():
    assert Solution().maxRepeating("ababc", "ab") == 2
    assert Solution().maxRepeating("ababc", "ba") == 1
    assert Solution().maxRepeating("ababc", "ac") == 0
    assert Solution().maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba") == 5
