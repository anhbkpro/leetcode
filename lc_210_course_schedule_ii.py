from collections import deque
from typing import List


def find_order(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    indegree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]

    for pair in prerequisites:
        second, first = pair
        indegree[second] += 1
        adj[first].append(second)

    q = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)

    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for neighbor in adj[node]:
            # Delete the edge "node -> neighbor".
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if any(indegree):
        return []

    return res


class Solution:
    pass
