from collections import deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for pair in prerequisites:
        second, first = pair
        indegree[second] += 1
        adj[first].append(second)

    q = deque()
    for item in range(numCourses):
        if indegree[item] == 0:
            q.append(item)

    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    if any(indegree):
        return False

    return True


class Solution:
    pass
