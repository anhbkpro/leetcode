from lc_2785_sort_vowels_in_a_string import Solution


def test_sort_vowels():
    assert Solution.sortVowels(s="lEetcOde") == "lEOtcede"
    assert Solution.sortVowels(s="lYmpH") == "lYmpH"
