from lc_688_knight_probability_in_chessboard import knight_probability


def test_knight_probability():
    assert knight_probability(n=3, k=2, row=0, column=0) == 0.0625
    assert knight_probability(n=1, k=0, row=0, column=0) == 1.0
