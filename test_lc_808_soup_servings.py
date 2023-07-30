from lc_808_soup_servings import Solution


def test_soup_servings():
    assert Solution().soupServings(50) == 0.625
    assert Solution().soupServings(100) == 0.71875
