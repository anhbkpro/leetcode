from .find_if_path_exists_in_graph import Solution


def test_valid_path():
    assert Solution().valid_path(n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2) == True
    assert Solution().valid_path(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5) == False
