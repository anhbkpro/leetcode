from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1

        q = deque([x for x in range(len(in_degree)) if in_degree[x] == 0])
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        if any(in_degree):
            return False

        return True
