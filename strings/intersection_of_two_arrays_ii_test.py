from strings.intersection_of_two_arrays_ii import Solution


def test_intersection_of_two_arrays():
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert sorted(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]
