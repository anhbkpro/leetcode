from hashing.longest_substring_without_repeating_characters import Solution


def test_longest_substring_without_repeating_characters():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
