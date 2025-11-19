from binary_search.minimize_the_maximum_difference_of_pairs import Solution


def test_single_element():
    solution = Solution()
    assert solution.minimizeMax([1], 0) == 0


def test_two_elements():
    solution = Solution()
    assert solution.minimizeMax([1, 2], 1) == 1
    assert solution.minimizeMax([2, 1], 1) == 1


def test_three_elements():
    solution = Solution()
    assert solution.minimizeMax([1, 2, 3], 1) == 1
    assert solution.minimizeMax([3, 1, 2], 1) == 1


def test_four_elements():
    solution = Solution()
    assert solution.minimizeMax([1, 2, 3, 4], 2) == 1
    assert solution.minimizeMax([4, 1, 2, 3], 2) == 1


def test_negative_numbers():
    solution = Solution()
    assert solution.minimizeMax([-1, -2, -3, -4], 2) == 1
    assert solution.minimizeMax([-4, -3, -2, -1], 2) == 1


def test_mixed_numbers():
    solution = Solution()
    assert solution.minimizeMax([1, -2, 3, -4], 2) == 2
    assert solution.minimizeMax([-4, 1, -2, 3], 2) == 2


def test_large_numbers():
    solution = Solution()
    assert solution.minimizeMax([1000, 2000, 3000, 4000], 2) == 1000
    assert solution.minimizeMax([4000, 1000, 2000, 3000], 2) == 1000


def test_leetcode_example():
    solution = Solution()
    assert solution.minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1
    assert solution.minimizeMax([4, 2, 1, 2], 1) == 0


def test_no_pairs():
    solution = Solution()
    assert solution.minimizeMax([1, 2, 3, 4], 0) == 0


def test_all_pairs():
    solution = Solution()
    assert solution.minimizeMax([1, 2, 3, 4], 2) == 1
    assert solution.minimizeMax([1, 2, 3, 4, 5, 6], 3) == 1
