from .maximal_range_that_each_element_is_maximum_in_it import Solution


def test_maximum_length_of_ranges():
    assert Solution().maximumLengthOfRanges(nums=[1, 5, 4, 3, 6]) == [1, 4, 2, 1, 5]
