from typing import List


def sequence_reconstruction(nums: List[int], sequences: List[List[int]]) -> bool:
    n = len(nums)
    indegree = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]

    for sequence in sequences:
        for idx in range(len(sequence) - 1):
            second, first = sequence[idx], sequence[idx + 1]
            indegree[second] += 1
            adj[first].append(second)

    q = [i for i in range(1, n + 1) if indegree[i] == 0]

    if len(q) > 1:
        return False

    while q:
        node = q.pop()
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
                if len(q) > 1:  # so this means there are more than one supersequence
                    return False

    return True


class Solution:
    pass
