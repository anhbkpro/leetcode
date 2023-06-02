import collections
from typing import List


def maximumDetonation(bombs: List[List[int]]) -> int:
    graph = collections.defaultdict(list)
    n = len(bombs)

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            xi, yi, ri = bombs[i]
            xj, yj, _ = bombs[j]

            # Create a path from node i to node j, if bomb i detonates bomb j.
            if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                graph[i].append(j)

    # DFS to get the number of nodes reachable from a given node cur
    def dfs(cur, seen):
        seen.add(cur)
        for neighbor in graph[cur]:
            if neighbor not in seen:
                dfs(neighbor, seen)
        return len(seen)

    answer = 0
    for i in range(n):
        visited = set()
        answer = max(answer, dfs(i, visited))

    return answer


class Solution:
    pass
