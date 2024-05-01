from hashing.longest_repeating_substring import Solution


def test_longest_repeating_substring():
    assert Solution().longestRepeatingSubstring("abbaba") == 2
    assert Solution().longestRepeatingSubstring("aabcaabdaab") == 3
