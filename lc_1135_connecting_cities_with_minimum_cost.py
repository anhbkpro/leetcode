from typing import List


class DisjoinSet:
    def __init__(self, n):
        self.rank = [1] * (n + 1)
        self.parents = [i for i in range(n + 1)]

    def find(self, a):
        """
        Find the root of a node.
        :param a: node a
        :return: root of a node
        """
        while a != self.parents[a]:
            a = self.parents[a]

        return a

    def union(self, a, b):
        """
        Union two nodes
        :param a: node a
        :param b: node b
        :return: None
        """
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        self.parents[root_b] = root_a

    def is_in_same_group(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    @staticmethod
    def minimum_cost(n: int, connections: List[List[int]]) -> int:
        ds = DisjoinSet(n)
        # sort connections by cost in ascending order
        connections = sorted(connections, key=lambda x: x[2])
        # total cost
        total_cost = 0
        # total edges
        total_edges = 0
        for conn in connections:
            # if two nodes are already in the same group, skip
            if ds.is_in_same_group(conn[0], conn[1]):
                continue
            # otherwise, union two nodes
            ds.union(conn[0], conn[1])
            # add cost
            total_cost += conn[2]
            # increase total edges
            total_edges += 1

        if total_edges == n - 1:
            return total_cost

        return -1
