from typing import List


def minReorder(n: int, connections: List[List[int]]) -> int:
    adj_list = [[] for _ in range(n)]
    for connection in connections:
        adj_list[connection[0]].append((connection[1], 1))  # 1 means the direction is reversed
        adj_list[connection[1]].append((connection[0], 0))  # 0 means the direction is not reversed
    queue = [(0, 0)]
    visited = set()
    visited.add(0)
    count = 0
    while queue:
        node, direction = queue.pop(0)
        for neighbor in adj_list[node]:
            if neighbor[0] not in visited:
                visited.add(neighbor[0])
                queue.append((neighbor[0], neighbor[1]))
                count += neighbor[1]
    return count


class Solution:
    pass
