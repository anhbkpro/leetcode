from .sort_array_by_increasing_frequency import Solution


def test_sort_array_by_increasing_frequency():
    assert Solution().frequencySort([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]
