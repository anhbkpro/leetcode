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
        # vertex = 0 -> 0 == 0 -> True -> return 0
        # vertex = 1 -> 1 == 1 -> True -> return 1
        if vertex == representative[vertex]:
            return vertex

        representative[vertex] = self.find(representative, representative[vertex])
        return representative[vertex]

    def combine(
        self, representative: List[int], size: List[int], vertex1: int, vertex2: int
    ) -> int:
        vertex1 = self.find(representative, vertex1) # 0
        vertex2 = self.find(representative, vertex2) # 1

        if vertex1 == vertex2:
            return 0
        else:
            if size[vertex1] > size[vertex2]:
                size[vertex1] += size[vertex2]
                representative[vertex2] = vertex1
            else:
                # size[0] = 1
                # size[1] = 1
                # size[0] += size[1] -> 1 += 1 -> 2
                # representative[1] = 0
                # representative[0] = 0
                size[vertex2] += size[vertex1]
                representative[vertex1] = vertex2
            return 1

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Example with Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        # Output: 2
        representative: List[int] = [i for i in range(n)] # [0, 1, 2, 3, 4]
        size: List[int] = [1] * n # [1, 1, 1, 1, 1]

        components: int = n
        for edge in edges:
            components -= self.combine(representative, size, edge[0], edge[1])
            # edge = [0, 1]
            # components -= self.combine(representative, size, edge[0], edge[1])
            # components -= self.combine(representative, size, 0, 1)
            # components -= 1
            # components = 4
        return components
