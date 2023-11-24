from lc_1598_crawler_log_folder import Solution


def test_min_operations():
    assert Solution.minOperations(logs=["d1/", "d2/", "../", "d21/", "./"]) == 2
    assert Solution.minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"]) == 3
    assert Solution.minOperations(logs=["d1/", "../", "../", "../"]) == 0
