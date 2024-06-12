from .sort_colors import Solution


def test_sortColors():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    Solution().sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [0]
    Solution().sortColors(nums)
    assert nums == [0]

    nums = [1]
    Solution().sortColors(nums)
    assert nums == [1]
