from .special_array_ii import SolutionBinarySearch, SolutionPrefixSum


def test_is_array_special():
    assert SolutionBinarySearch().isArraySpecial(
        nums=[3, 4, 1, 2, 6], queries=[[0, 4]]
    ) == [False]
    assert SolutionBinarySearch().isArraySpecial(
        nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]
    ) == [
        False,
        True,
    ]
    assert SolutionPrefixSum().isArraySpecial(
        nums=[3, 4, 1, 2, 6], queries=[[0, 4]]
    ) == [False]
    assert SolutionPrefixSum().isArraySpecial(
        nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]
    ) == [
        False,
        True,
    ]
