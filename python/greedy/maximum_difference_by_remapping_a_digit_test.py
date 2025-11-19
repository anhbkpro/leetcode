from greedy.maximum_difference_by_remapping_a_digit import Solution


def test_single_digit():
    solution = Solution()
    assert solution.minMaxDifference(1) == 9
    assert solution.minMaxDifference(9) == 9


def test_two_digits():
    solution = Solution()
    assert solution.minMaxDifference(10) == 90
    assert solution.minMaxDifference(99) == 99
    assert solution.minMaxDifference(12) == 90


def test_three_digits():
    solution = Solution()
    assert solution.minMaxDifference(100) == 900
    assert solution.minMaxDifference(999) == 999
    assert solution.minMaxDifference(123) == 900


def test_four_digits():
    solution = Solution()
    assert solution.minMaxDifference(1000) == 9000
    assert solution.minMaxDifference(9999) == 9999
    assert solution.minMaxDifference(1234) == 9000


def test_all_nines():
    solution = Solution()
    assert solution.minMaxDifference(9) == 9
    assert solution.minMaxDifference(99) == 99
    assert solution.minMaxDifference(999) == 999
    assert solution.minMaxDifference(9999) == 9999


def test_all_zeros():
    solution = Solution()
    assert solution.minMaxDifference(0) == 9
    assert solution.minMaxDifference(00) == 9
    assert solution.minMaxDifference(000) == 9
    assert solution.minMaxDifference(0000) == 9


def test_leetcode_examples():
    solution = Solution()
    assert solution.minMaxDifference(11891) == 99009
    assert solution.minMaxDifference(90) == 99


def test_repeated_digits():
    solution = Solution()
    assert solution.minMaxDifference(111) == 999
    assert solution.minMaxDifference(222) == 999
    assert solution.minMaxDifference(333) == 999


def test_ascending_digits():
    solution = Solution()
    assert solution.minMaxDifference(123) == 900
    assert solution.minMaxDifference(1234) == 9000
    assert solution.minMaxDifference(12345) == 90000


def test_descending_digits():
    solution = Solution()
    assert solution.minMaxDifference(321) == 900
    assert solution.minMaxDifference(4321) == 9000
    assert solution.minMaxDifference(54321) == 90000
