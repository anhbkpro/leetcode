from typing import List


class DisjoinSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parents = [i for i in range(n + 1)]

    def find(self, a):
        while a != self.parents[a]:
            a = self.parents[a]
        return a

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        self.parents[root_b] = root_a

    def is_in_same_root(self, a, b):
        return self.find(a) == self.find(b)


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
                    weights.append([i, j, distance])
        weights = sorted(weights, key=lambda x: x[2])
        ds = DisjoinSet(n)
        total_cost = 0
        total_edges = 0
        for weight in weights:
            if ds.is_in_same_root(weight[0], weight[1]):
                continue
            ds.union(weight[0], weight[1])
            total_cost += weight[2]
            total_edges += 1

        if total_edges == n - 1:
            return total_cost

        return 0
