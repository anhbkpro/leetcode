from .minimum_number_of_swaps_to_make_the_string_balanced import Solution


def test_minimum_number_of_swaps_to_make_the_string_balanced():
    assert Solution().minSwaps("][][") == 1
    assert Solution().minSwaps("]]][[[") == 2
    assert Solution().minSwaps("[]") == 0
