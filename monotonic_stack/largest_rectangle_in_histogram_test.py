from monotonic_stack.largest_rectangle_in_histogram import Solution


def test_largestRectangleArea():
    assert Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert Solution().largestRectangleArea([2, 4]) == 4
