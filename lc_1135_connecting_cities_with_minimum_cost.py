from typing import List


class UnionFind:
    def __init__(self, n):
        self.rank = [1] * (n + 1)
        self.parents = [i for i in range(n + 1)]

    def find(self, a):
        """
        Find the root of a node.
        :param a: node a
        :return: root of a node
        """
        # path compression
        while a != self.parents[a]:
            a = self.parents[a]

        return a

    def join(self, a, b) -> bool:
        """
        Union two nodes
        :param a: node a
        :param b: node b
        :return: None
        """
        root_a = self.find(a)
        root_b = self.find(b)

        # if two nodes are already in the same group, skip
        if root_a == root_b:
            return False

        # otherwise, union two nodes
        self.parents[root_b] = root_a
        return True

    def is_in_same_group(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    @staticmethod
    def minimum_cost(n: int, connections: List[List[int]]) -> int:
        ds = UnionFind(n)
        connections = sorted(connections, key=lambda x: x[2])
        total_cost = 0
        total_edges = 0

        for conn in connections:
            if ds.join(conn[0], conn[1]):
                total_cost += conn[2]
                total_edges += 1

        if total_edges == n - 1:
            return total_cost

        return -1
