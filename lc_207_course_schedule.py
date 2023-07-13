from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    adj = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for pair in prerequisites:
        second, first = pair
        indegree[second] += 1
        adj[first].append(second)

    q = [c for c in indegree if indegree[c] == 0]

    nodes_visited = 0
    while q:
        node = q.pop()
        nodes_visited += 1

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # if any(indegree):
    #     return False
    #
    # return True
    return nodes_visited == num_courses  # this is the same as the above commented out code


class Solution:
    pass
