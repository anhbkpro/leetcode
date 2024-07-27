from .minimum_cost_to_convert_string_i import Solution


def test_minimum_cost():
    assert (
        Solution().minimumCost(
            source = "abcd",
            target = "acbe",
            original = ["a","b","c","c","e","d"],
            changed = ["b","c","b","e","b","e"],
            cost = [2,5,5,1,2,20]
        )
        == 28
    )
    assert (
        Solution().minimumCost(
            source = "aaaa",
            target = "bbbb",
            original = ["a","c"],
            changed = ["c","b"],
            cost = [1,2]
        )
        == 12
    )
