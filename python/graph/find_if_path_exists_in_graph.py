from typing import List
from collections import deque


class Solution:
    def valid_path(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        q = deque([source])
        while q:
            node = q.popleft()
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    q.append(neighbor)

        return False
