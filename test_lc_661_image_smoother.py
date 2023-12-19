from lc_661_image_smoother import Solution


def test_image_smoother():
    assert Solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert Solution.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137],
                                                                                          [141, 138, 141],
                                                                                          [137, 141, 137]]
