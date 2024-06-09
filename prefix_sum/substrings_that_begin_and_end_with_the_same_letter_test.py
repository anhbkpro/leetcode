from .substrings_that_begin_and_end_with_the_same_letter import Solution


def test_substrings_that_begin_and_end_with_the_same_letter():
  assert Solution().numberOfSubstrings("abcba") == 7
  assert Solution().numberOfSubstrings("abacad") == 9
  assert Solution().numberOfSubstrings("a") == 1
