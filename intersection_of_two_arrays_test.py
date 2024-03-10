from intersection_of_two_arrays import Solution

solution = Solution()


def test_intersection():
    assert solution.intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert solution.intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
