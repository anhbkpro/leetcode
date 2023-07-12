from collections import deque
from typing import List


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    indegree = [0] * n  # indegree[i] contains no of outgoing edges at node i
    adj = [[] for _ in range(n)]

    # [[1,2],[2,3],[5],[0],[5],[],[]]
    for i in range(n):
        for node in graph[i]:
            # adj[1] = [0] adj[2] = [0, 1] adj[3] = [1] adj[5] = [2] adj[0] = [3] adj[4] = [5] adj[5] = adj[6] = []
            adj[node].append(i)
            indegree[i] += 1
    # node 0 has 2 outgoing edges
    # node 1 has 2 outgoing edges
    # node 2 has 1 outgoing edges
    # node 3 has 1 outgoing edges
    # node 4 has 1 outgoing edges
    # node 5 and 6 have 0 outgoing edges => so they are 2 terminal nodes.

    # A node is a `safe node` if every possible path starting from that node leads to a terminal node (or another
    # safe node). => so a `terminal node` is also a safe node.
    q = deque()
    # Push all the nodes with indegree zero in the queue.
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)  # [5, 6] terminal nodes (A node is a terminal node if there are no outgoing edges.)

    print(adj)
    print(indegree)
    print(q)

    safe = [False] * n
    while q:
        node = q.popleft()
        safe[node] = True

        for neighbor in adj[node]:
            # Delete the edge "node -> neighbor".
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    safe_nodes = []
    for i in range(n):
        if safe[i]:
            safe_nodes.append(i)

    print(safe_nodes)

    return safe_nodes


class Solution:
    pass
