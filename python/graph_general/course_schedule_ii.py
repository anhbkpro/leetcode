from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for second, first in prerequisites:
            graph[first].append(second)
            indegree[second] += 1

        q = deque([course for course in range(numCourses) if indegree[course] == 0])
        if not graph:
            return list(range(numCourses))

        visited = [False] * numCourses
        ans = []
        while q:
            node = q.popleft()
            visited[node] = True
            ans.append(node)

            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(ans) < numCourses:  # this is a cyclic graph
            return []

        return ans
