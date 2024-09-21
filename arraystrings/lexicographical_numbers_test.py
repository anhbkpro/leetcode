from .lexicographical_numbers import Solution


def test_lexical_order():
    assert Solution().lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution().lexicalOrder(2) == [1, 2]
