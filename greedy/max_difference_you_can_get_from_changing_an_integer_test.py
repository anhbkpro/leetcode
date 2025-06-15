from greedy.max_difference_you_can_get_from_changing_an_integer import Solution


def test_single_digit():
    solution = Solution()
    assert solution.maxDiff(1) == 8  # 9 - 1
    assert solution.maxDiff(9) == 8  # 9 - 1


def test_two_digits():
    solution = Solution()
    assert solution.maxDiff(10) == 80  # 99 - 10
    assert solution.maxDiff(99) == 88  # 99 - 11
    assert solution.maxDiff(12) == 82  # 99 - 11


def test_three_digits():
    solution = Solution()
    assert solution.maxDiff(100) == 800  # 900 - 100
    assert solution.maxDiff(999) == 888  # 999 - 111
    assert solution.maxDiff(123) == 820  # 923 - 103


def test_four_digits():
    solution = Solution()
    assert solution.maxDiff(1000) == 8000  # 9999 - 1000
    assert solution.maxDiff(9999) == 8888  # 9999 - 1111
    assert solution.maxDiff(1234) == 8200  # 9999 - 1111


def test_all_nines():
    solution = Solution()
    assert solution.maxDiff(9) == 8  # 9 - 1
    assert solution.maxDiff(99) == 88  # 99 - 11
    assert solution.maxDiff(999) == 888  # 999 - 111
    assert solution.maxDiff(9999) == 8888  # 9999 - 1111


def test_all_ones():
    solution = Solution()
    assert solution.maxDiff(1) == 8  # 9 - 1
    assert solution.maxDiff(11) == 88  # 99 - 11
    assert solution.maxDiff(111) == 888  # 999 - 111
    assert solution.maxDiff(1111) == 8888  # 9999 - 1111


def test_leetcode_examples():
    solution = Solution()
    assert solution.maxDiff(555) == 888  # 999 - 111
    assert solution.maxDiff(9) == 8  # 9 - 1
    assert solution.maxDiff(123456) == 820000  # 999999 - 100000


def test_repeated_digits():
    solution = Solution()
    assert solution.maxDiff(111) == 888  # 999 - 111
    assert solution.maxDiff(222) == 888  # 999 - 111
    assert solution.maxDiff(333) == 888  # 999 - 111


def test_ascending_digits():
    solution = Solution()
    assert solution.maxDiff(123) == 820  # 999 - 111
    assert solution.maxDiff(1234) == 8200  # 9999 - 1111
    assert solution.maxDiff(12345) == 82000  # 99999 - 11111


def test_descending_digits():
    solution = Solution()
    assert solution.maxDiff(321) == 800  # 999 - 111
    assert solution.maxDiff(4321) == 8000  # 9999 - 1111
    assert solution.maxDiff(54321) == 80000  # 99999 - 11111


def test_mixed_digits():
    solution = Solution()
    assert solution.maxDiff(102) == 802  # 999 - 111
    assert solution.maxDiff(203) == 800  # 999 - 111
    assert solution.maxDiff(304) == 800  # 999 - 111
