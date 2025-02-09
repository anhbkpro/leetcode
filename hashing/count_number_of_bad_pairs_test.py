import hashing.count_number_of_bad_pairs as Solution


def test_example_1():
    solution = Solution.Solution()
    nums = [4, 1, 3, 3]
    expected = 5
    assert solution.countBadPairs(nums) == expected


def test_example_2():
    solution = Solution.Solution()
    nums = [1, 2, 3, 4, 5]
    expected = 0
    assert solution.countBadPairs(nums) == expected
