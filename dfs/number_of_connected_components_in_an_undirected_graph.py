from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(visited, graph, node):
            if node in visited:
                return

            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                dfs(visited, graph, neighbor)

        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(visited, graph, i)

        return components
