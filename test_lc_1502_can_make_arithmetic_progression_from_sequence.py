from lc_1502_can_make_arithmetic_progression_from_sequence import canMakeArithmeticProgression


def test_can_make_arithmetic_progression():
    assert canMakeArithmeticProgression([3, 5, 1]) == True
    assert canMakeArithmeticProgression([1, 2, 4]) == False
