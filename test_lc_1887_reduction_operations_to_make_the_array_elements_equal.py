from lc_1887_reduction_operations_to_make_the_array_elements_equal import Solution


def test_reduction_operations():
    assert Solution.reductionOperations(nums=[5, 1, 3]) == 3
    assert Solution.reductionOperations(nums=[1, 1, 1]) == 0
