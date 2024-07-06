from .reveal_cards_in_increasing_order import Solution


def test_deck_revealed_increasing():
    assert Solution.deck_revealed_increasing(deck=[17, 13, 11, 2, 3, 5, 7]) == [2, 13, 3, 11, 5, 17, 7]
