from lc_1463_cherry_pickup_ii import Solution


def test_cherry_pickup():
    assert Solution.cherryPickup(grid=[[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]) == 24
assert Solution.cherryPickup(grid=[[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0], [1, 0, 2, 3, 0, 0, 6]]) == 28