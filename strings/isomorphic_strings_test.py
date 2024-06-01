from strings.isomorphic_strings import Solution


def test_isomorphic_strings():
    assert Solution.is_isomorphic(s="egg", t="add") is True
    assert Solution.is_isomorphic(s="foo", t="bar") is False
    assert Solution.is_isomorphic(s="paper", t="title") is True
