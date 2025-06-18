from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = [False] * len(rooms)

        while len(q) > 0:
            room = q.popleft()
            if not visited or visited[room]:
                continue
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    q.append(key)

        return all(visited)
