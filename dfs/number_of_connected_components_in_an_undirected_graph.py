from collections import defaultdict
from typing import List


class DFS:
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


class UnionFind:
    def find(self, representative, vertex):
        if vertex == representative[vertex]:
            return vertex

        representative[vertex] = self.find(representative, representative[vertex])
        return representative[vertex]

    def combine(self, representative, size, vertex1, vertex2):
        vertex1 = self.find(representative, vertex1)
        vertex2 = self.find(representative, vertex2)

        if vertex1 == vertex2:
            return 0
        else:
            if size[vertex1] > size[vertex2]:
                size[vertex1] += size[vertex2]
                representative[vertex2] = vertex1
            else:
                size[vertex2] += size[vertex1]
                representative[vertex1] = vertex2
            return 1

    def countComponents(self, n, edges):
        representative = [i for i in range(n)]
        size = [1] * n

        components = n
        for edge in edges:
            components -= self.combine(representative, size, edge[0], edge[1])

        return components
