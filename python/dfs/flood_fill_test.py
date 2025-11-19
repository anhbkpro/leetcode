from .flood_fill import Solution


def test_flood_fill():
    # Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
    # Output: [[2,2,2],[2,2,0],[2,0,1]]
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    expected = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert Solution().floodFill(image, sr, sc, color) == expected
