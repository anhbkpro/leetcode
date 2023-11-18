from lc_1838_frequency_of_the_most_frequent_element import Solution


def test_max_frequency():
    assert Solution.maxFrequency(nums=[1, 2, 4], k=5) == 3
    assert Solution.maxFrequency(nums=[1, 4, 8, 13], k=5) == 2
