from maximum_nesting_depth_of_the_parentheses import Solution


def test_max_depth():
    s = Solution()
    assert s.max_depth("(1+(2*3)+((8)/4))+1") == 3
    assert s.max_depth("(1)+((2))+(((3)))") == 3
    assert s.max_depth("1+(2*3)/(2-1)") == 1
