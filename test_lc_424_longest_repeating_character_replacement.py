from lc_424_longest_repeating_character_replacement import Solution


def test_character_replacement():
    assert Solution.character_replacement(s="ABAB", k=2) == 4
    assert Solution.character_replacement(s="AABABBA", k=1) == 4
