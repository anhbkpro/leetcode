from .valid_arrangement_of_pairs import Solution


def test_valid_arrangement():
    assert Solution().validArrangement(pairs=[[5, 1], [4, 5], [11, 9], [9, 4]]) == [
        [11, 9],
        [9, 4],
        [4, 5],
        [5, 1],
    ]
