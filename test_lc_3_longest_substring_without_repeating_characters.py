from lc_3_longest_substring_without_repeating_characters import Solution


def test_length_of_longest_substring():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
