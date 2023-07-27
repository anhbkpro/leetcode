from lc_2141_maximum_running_time_of_n_computers import Solution


def test_max_run_time():
    assert Solution.maxRunTime(n=3, batteries=[2, 3, 5]) == 2
    assert Solution.maxRunTime(n=3, batteries=[1, 1, 1]) == 1
