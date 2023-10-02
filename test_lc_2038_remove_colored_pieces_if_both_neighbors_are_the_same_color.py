from lc_2038_remove_colored_pieces_if_both_neighbors_are_the_same_color import Solution


def test_winner_of_game():
    assert Solution.winnerOfGame(colors="AAABABB") is True
    assert Solution.winnerOfGame(colors="AA") is False
