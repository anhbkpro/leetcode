from lc_1420_build_array_where_you_can_find_the_maximum_exactly_k_comparisons import *


def test_num_of_arrays():
    assert Solution.numOfArrays(n=2, m=3, k=1) == 6
    assert Solution.numOfArrays(n=5, m=2, k=3) == 0
