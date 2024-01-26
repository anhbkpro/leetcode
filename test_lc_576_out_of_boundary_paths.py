from lc_576_out_of_boundary_paths import Solution

solution = Solution()


def test_find_paths():
    assert solution.findPaths(m=2, n=2, maxMove=2, startRow=0, startColumn=0) == 6
    assert solution.findPaths(m=1, n=3, maxMove=3, startRow=0, startColumn=1) == 12
