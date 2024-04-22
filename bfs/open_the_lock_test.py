from bfs.open_the_lock import Solution


def test_open_lock():
    assert Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
    assert Solution().openLock(["8888"], "0009") == 1
    assert Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1
    assert Solution().openLock(["0000"], "8888") == -1
