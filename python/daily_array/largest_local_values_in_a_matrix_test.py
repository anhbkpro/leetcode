from daily_array.largest_local_values_in_a_matrix import Solution


def test_largest_local_values_in_a_matrix():
    assert Solution().largestLocal(
        [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
    ) == [[9, 9], [8, 6]]
    assert Solution().largestLocal(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    ) == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
