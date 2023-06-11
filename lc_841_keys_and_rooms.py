from collections import deque
from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    seen = [False]*len(rooms)
    q = deque()
    q.append(0)
    seen[0] = True
    while q:
        room = q.popleft()
        for key in rooms[room]:
            if not seen[key]:
                seen[key] = True
                q.append(key)

    return all(seen)


class Solution:
    pass
