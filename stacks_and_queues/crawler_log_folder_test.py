from .crawler_log_folder import Solution


def test_crawler_log_folder():
    solution = Solution()

    logs = ["d1/", "d2/", "../", "d21/", "./"]
    assert solution.minOperations(logs) == 2

    logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
    assert solution.minOperations(logs) == 3

    logs = ["d1/", "../", "../", "../"]
    assert solution.minOperations(logs) == 0
