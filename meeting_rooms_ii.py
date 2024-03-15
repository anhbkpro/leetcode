import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        free_rooms = []
        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        heapq.heappush(free_rooms, intervals[0][1])

        for start, end in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms and free_rooms[0] <= start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap.
            heapq.heappush(free_rooms, end)

        return len(free_rooms)
