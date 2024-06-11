from .find_common_characters import Solution


def test_find_common_characters():
    assert sorted(Solution().commonChars(["bella", "label", "roller"])) == ["e", "l", "l"]
    assert sorted(Solution().commonChars(["cool", "lock", "cook"])) == ["c", "o"]
