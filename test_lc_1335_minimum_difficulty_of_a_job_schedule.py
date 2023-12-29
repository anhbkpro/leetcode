from lc_1335_minimum_difficulty_of_a_job_schedule import Solution


def test_min_difficulty():
    assert Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7
    assert Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4) == -1
    assert Solution().minDifficulty(jobDifficulty=[1, 1, 1], d=3) == 3


def test_min_difficulty_top_down():
    assert Solution().minDifficultyTopDown(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2) == 7
    assert Solution().minDifficultyTopDown(jobDifficulty=[9, 9, 9], d=4) == -1
    assert Solution().minDifficultyTopDown(jobDifficulty=[1, 1, 1], d=3) == 3
