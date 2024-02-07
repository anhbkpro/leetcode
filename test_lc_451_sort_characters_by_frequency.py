from lc_451_sort_characters_by_frequency import Solution


def test_frequency_sort():
    assert Solution.frequencySort(s="tree") == "eetr"
    assert Solution.frequencySort(s="cccaaa") == "cccaaa"
