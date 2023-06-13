from lc_2300_successful_pairs_of_spells_and_potions import successful_pairs


def test_successful_pairs():
    assert successful_pairs(spells=[5, 1, 3], potions=[1, 2, 3, 4, 5], success=7) == [4, 0, 3]
    assert successful_pairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16) == [2, 0, 2]
