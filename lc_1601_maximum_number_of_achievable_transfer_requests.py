import itertools


def maximumRequests(n, req):
    for k in range(len(req), 0, -1):
        # https://docs.python.org/3/library/itertools.html#itertools.combinations
        for c in itertools.combinations(range(len(req)), k):
            degree = [0] * n
            for i in c:
                degree[req[i][0]] -= 1
                degree[req[i][1]] += 1
            if not any(degree):  # all(degree[i] == 0 for i in range(n)): For example: degree: [0, 0, 0, 0, 0]
                return k
    return 0


class Solution:
    pass
