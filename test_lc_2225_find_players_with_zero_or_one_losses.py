from lc_2225_find_players_with_zero_or_one_losses import Solution


def test_find_winners():
    assert Solution().findWinners(
        matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]) == [[1, 2, 10],
                                                                                                        [4, 5, 7, 8]]
    assert Solution().findWinners(matches=[[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]
