from .find_the_winner_of_the_circular_game import Solution


def test_find_the_winner_of_the_circular_game():
    assert Solution().findTheWinner(n=5, k=2) == 3
    assert Solution().findTheWinner(n=6, k=5) == 1
