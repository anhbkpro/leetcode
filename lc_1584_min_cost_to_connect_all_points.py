from typing import List


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]

    def find(self, a):
        while a != self.parents[a]:
            a = self.parents[a]
        return a

    def join(self, a, b) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        self.parents[root_b] = root_a
        return True


class Solution:
    @staticmethod
    def minCostConnectPoints(points: List[List[int]]) -> int:
        weights = []
        visited = {}
        n = len(points)
        for i in range(1, n):
            for j in range(i):
                if (i, j) in visited:
                    continue
                else:
                    distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    visited[(i, j)] = True
                    weights.append([distance, i, j])

        weights.sort()
        ds = UnionFind(n)
        total_cost = 0
        total_edges = 0
        for weight, node1, node2 in weights:
            if ds.join(node1, node2):
                total_cost += weight
                total_edges += 1

        if total_edges == n - 1:
            return total_cost

        return 0
