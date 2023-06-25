from lc_531_lonely_pixel_i import findLonelyPixel


def test_find_lonely_pixel():
    assert findLonelyPixel([['W', 'W', 'B'], ['W', 'B', 'W'], ['B', 'W', 'W']]) == 3
    assert findLonelyPixel([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]) == 0
