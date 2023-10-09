from lc_34_find_first_and_last_position_of_element_in_sorted_array import Solution

solution = Solution()


def test_search_range():
    assert solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4]
    assert solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1]
    assert solution.searchRange(nums=[], target=0) == [-1, -1]
    assert solution.searchRange(nums=[1], target=1) == [0, 0]
    assert solution.searchRange(nums=[2, 2], target=2) == [0, 1]
