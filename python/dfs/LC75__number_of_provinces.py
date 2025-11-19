from typing import List


class Solution:
    def dfs(self, node, isConnected, visited):
        visited[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] and not visited[i]:
                self.dfs(i, isConnected, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        number_of_components = 0
        visited = [False] * size
        for city in range(size):
            if not visited[city]:
                number_of_components += 1
                self.dfs(city, isConnected, visited)

        return number_of_components
