from lc_46_permutations import Solution


def test_permute():
    assert Solution.permute(nums=[1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]]
    assert Solution.permute(nums=[0, 1]) == [[0, 1], [1, 0]]
