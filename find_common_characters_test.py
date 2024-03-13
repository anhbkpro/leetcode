from find_common_characters import Solution

solution = Solution()


def test_find_common_chars():
    assert sorted(solution.commonChars(["bella", "label", "roller"])) == sorted(
        ["e", "l", "l"]
    )
    assert sorted(solution.commonChars(["cool", "lock", "cook"])) == ["c", "o"]
