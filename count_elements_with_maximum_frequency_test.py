from count_elements_with_maximum_frequency import Solution


def test_count_elements_with_max_freq():
    assert Solution.maxFrequencyElements([1, 2, 2, 3, 1]) == 2
    assert Solution.maxFrequencyElements([1, 2, 2, 3, 1, 3, 3]) == 3
