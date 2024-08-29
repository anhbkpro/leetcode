from .most_stones_removed_with_same_row_or_column import Solution


def test_most_stones_removed_with_same_row_or_column():
    assert Solution().removeStones(stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]) == 5
    assert Solution().removeStones(stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]) == 3


