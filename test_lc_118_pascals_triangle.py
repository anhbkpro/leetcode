from lc_118_pascals_triangle import Solution


def test_generate():
    assert Solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
                                    [1, 4, 6, 4, 1]]
