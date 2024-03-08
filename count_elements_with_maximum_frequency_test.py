from count_elements_with_maximum_frequency import Solution


def test_count_elements_with_max_freq():
    assert Solution.max_frequency_elements([1, 2, 2, 3, 1]) == 4
    assert Solution.max_frequency_elements([1, 4, 4, 4, 5, 3]) == 3
    assert Solution.max_frequency_elements([1, 2, 3, 4, 5]) == 5
