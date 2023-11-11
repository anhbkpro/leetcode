from collections import defaultdict
from typing import List


class Solution:
    @staticmethod
    def restoreArray(adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                print(f"neighbor {neighbor} of node {node}")
                if neighbor != prev:
                    print(f"-- dfs neighbor {neighbor}")
                    dfs(neighbor, node, ans)

        ans = []
        dfs(root, None, ans)
        return ans
