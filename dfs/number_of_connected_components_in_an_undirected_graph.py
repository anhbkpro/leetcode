from collections import defaultdict
from typing import List, Set, Dict


class DFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(visited: Set[int], graph: Dict[int, List[int]], node: int) -> None:
            if node in visited:
                return

            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                dfs(visited, graph, neighbor)

        visited: Set[int] = set()
        graph: Dict[int, List[int]] = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        components: int = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(visited, graph, i)

        return components


class UnionFind:
    def find(self, representative: List[int], vertex: int) -> int:
        if vertex == representative[vertex]:
            return vertex

        representative[vertex] = self.find(representative, representative[vertex])
        return representative[vertex]

    def combine(
        self, representative: List[int], size: List[int], vertex1: int, vertex2: int
    ) -> int:
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

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        representative: List[int] = [i for i in range(n)]
        size: List[int] = [1] * n

        components: int = n
        for edge in edges:
            components -= self.combine(representative, size, edge[0], edge[1])

        return components
