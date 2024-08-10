from .regions_cut_by_slashes import Solution


def test_regions_by_slashes():
    # Input: grid = [" /","/ "]
    # Output: 2
    assert Solution().regionsBySlashes([" /", "/ "]) == 2
    # Input: grid = [" /","  "]
    # Output: 1
    assert Solution().regionsBySlashes([" /", "  "]) == 1
    # Input: grid = ["/\\","\\/"]
    # Output: 5
    assert Solution().regionsBySlashes(["/\\", "\\/"]) == 5
