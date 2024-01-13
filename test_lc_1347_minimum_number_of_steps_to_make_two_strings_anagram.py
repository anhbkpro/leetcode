from lc_1347_minimum_number_of_steps_to_make_two_strings_anagram import Solution


def test_min_steps():
    assert Solution().minSteps("bab", "aba") == 1
    assert Solution().minSteps("leetcode", "practice") == 5
