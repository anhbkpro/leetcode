from .take_k_of_each_character_from_left_and_right import Solution


def test_take_k_of_each_character_from_left_and_right():
    assert Solution().takeCharacters(s="aabaaaacaabc", k=2) == 8
    assert Solution().takeCharacters(s="a", k=1) == -1
