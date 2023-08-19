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
        # path compression
        print(f"find root of {a}: ")
        tmp = a
        while a != self.parents[a]:
            print(f"continue find root of {a} = {self.parents[a]}")
            a = self.parents[a]

        print(f"===> root of {tmp} is {a}")
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

        # if two nodes are already in the same group, skip
        if root_a == root_b:
            print(f"{a} and {b} are already in the same group")
            return

        # otherwise, union two nodes
        # union by rank
        print(f"union {a} and {b}, so {root_a} and {root_b} are in the same group = {root_a}")
        self.parents[root_b] = root_a

    def is_in_same_group(self, a, b):
        # if two nodes are in the same group, they have the same root
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
            print(f"1. Consider {conn[0]} and {conn[1]}")
            # if two nodes are already in the same group, skip
            if ds.is_in_same_group(conn[0], conn[1]):
                print(f"2. {conn[0]} and {conn[1]} are already in the same group")
                continue
            # otherwise, union two nodes
            print(f"2. union {conn[0]} and {conn[1]}")
            ds.union(conn[0], conn[1])
            # add cost
            total_cost += conn[2]
            # increase total edges
            total_edges += 1

        if total_edges == n - 1:
            return total_cost

        return -1
