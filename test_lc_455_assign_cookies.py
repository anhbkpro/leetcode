from lc_455_assign_cookies import Solution


def test_find_content_children():
    assert Solution().findContentChildren(g=[1, 2, 3], s=[1, 1]) == 1
    assert Solution().findContentChildren(g=[1, 2], s=[1, 2, 3]) == 2
    assert Solution().findContentChildren(g=[10, 9, 8, 7], s=[5, 6, 7, 8]) == 2
