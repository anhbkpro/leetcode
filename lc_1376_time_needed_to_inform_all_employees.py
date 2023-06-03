from typing import List


class Solution:
    def dfs(self, manager, informTime, adjList):
        max_time = 0
        for subordinate in adjList[manager]:
            max_time = max(max_time, self.dfs(subordinate, informTime, adjList))
        return max_time + informTime[manager]

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                adj_list[m].append(i)
        return self.dfs(headID, informTime, adj_list)
