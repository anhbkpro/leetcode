from .minimum_number_of_swaps_to_make_the_string_balanced import Solution


def test_minimum_number_of_swaps_to_make_the_string_balanced():
    assert Solution().min_swaps_stack("][][") == 1
    assert Solution().min_swaps_stack("]]][[[") == 2
    assert Solution().min_swaps_stack("[]") == 0
    assert Solution().min_swaps_space_optimized_stack("][][") == 1
    assert Solution().min_swaps_space_optimized_stack("]]][[[") == 2
    assert Solution().min_swaps_space_optimized_stack("[]") == 0
