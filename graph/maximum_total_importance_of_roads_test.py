from .maximum_total_importance_of_roads import Solution


def test_maximumImportance():
    assert Solution().maximumImportance(n = 5, roads = [[0,3],[2,4],[1,3]]) == 20
    assert Solution().maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) == 43
