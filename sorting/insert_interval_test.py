from .insert_interval import Solution


def test_insert():
    assert Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]) == [[1,5],[6,9]]
    assert Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]) == [[1,2],[3,10],[12,16]]
