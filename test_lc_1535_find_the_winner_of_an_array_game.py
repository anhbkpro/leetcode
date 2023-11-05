from lc_1535_find_the_winner_of_an_array_game import Solution


def test_get_winner():
    assert Solution().getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2) == 5
    assert Solution().getWinner(arr=[3, 2, 1], k=10) == 3
