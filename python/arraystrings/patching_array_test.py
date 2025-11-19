from .patching_array import Solution


def test_min_patches():
    assert Solution().minPatches([1, 3], 6) == 1
