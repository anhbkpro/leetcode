from collections import deque
from typing import List


def minimum_semesters(n: int, relations: List[List[int]]) -> int:
    indegree = [0] * n
    adj = [[] for _ in range(n)]

    for relation in relations:
        prev_course, next_course = relation
        indegree[next_course - 1] += 1
        adj[prev_course - 1].append(next_course - 1)

    if all(indegree):
        return -1

    q = deque([c for c in range(n) if indegree[c] == 0])
    ans = 0
    while q:
        count = len(q)
        ans += 1  # take all parallel courses at one
        for i in range(count):  # take all parallel courses at one
            node = q.popleft()
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                # delete edge -> this means all prerequisite courses learned
                if indegree[neighbor] == 0:
                    q.append(neighbor)

    if any(indegree):
        return -1

    return ans


class Solution:
    pass
