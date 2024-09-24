from .find_the_length_of_the_longest_common_prefix import Solution


def test_longest_common_prefix():
    assert Solution().longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000]) == 3
    assert Solution().longestCommonPrefix(arr1 = [1,2,3], arr2 = [4,4,4]) == 0
