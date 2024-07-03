from .buble_sort import Solution


def test_height_checker():
    assert Solution().heightChecker(heights = [1,1,4,2,1,3]) == 3
