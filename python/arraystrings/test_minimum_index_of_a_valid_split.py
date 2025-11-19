from .minimum_index_of_a_valid_split import Solution


def test_minimum_index_example1():
    solution = Solution()
    nums = [1, 2, 2, 2]
    assert solution.minimumIndex(nums) == 2


def test_minimum_index_example2():
    solution = Solution()
    nums = [2, 1, 3, 1, 1, 1, 7, 1, 2, 1]
    assert solution.minimumIndex(nums) == 4


def test_minimum_index_example3():
    solution = Solution()
    nums = [3, 3, 3, 3, 7, 2, 2]
    assert solution.minimumIndex(nums) == -1


def test_minimum_index_single_element():
    solution = Solution()
    nums = [1]
    assert solution.minimumIndex(nums) == -1


def test_minimum_index_two_elements():
    solution = Solution()
    nums = [1, 1]
    assert solution.minimumIndex(nums) == 0


def test_minimum_index_three_elements():
    solution = Solution()
    nums = [1, 2, 2]
    assert solution.minimumIndex(nums) == -1
