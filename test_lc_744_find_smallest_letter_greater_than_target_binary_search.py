from lc_744_find_smallest_letter_greater_than_target_binary_search import nextGreatestLetter


def test_next_greatest_letter():
    assert nextGreatestLetter(letters=["c", "f", "j"], target="a") == "c"
    assert nextGreatestLetter(letters=["c", "f", "j"], target="c") == "f"
    assert nextGreatestLetter(letters=["c", "f", "j"], target="d") == "f"
