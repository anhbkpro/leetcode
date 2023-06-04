from lc_1926_nearest_exit_from_entrance_in_maze import nearestExit


def test_nearest_exit():
    assert nearestExit(maze=[["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], entrance=[1, 2]) == 1
    assert nearestExit(maze=[["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], entrance=[1, 0]) == 2
    assert nearestExit(maze=[[".", "+"]], entrance=[0, 0]) == -1
