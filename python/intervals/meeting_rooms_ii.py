from typing import List
import heapq


class SolutionPriorityQueues:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        free_rooms = []
        heapq.heapify(free_rooms)
        for start, end in intervals:
            if free_rooms and free_rooms[0] <= start:
                # this means a meeting has ended, so we can reuse one of the existing rooms
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)
        return len(free_rooms)


class SolutionChronologicalOrdering:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        used_rooms = 0
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])

        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            if start_times[start_pointer] >= end_times[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            start_pointer += 1
            used_rooms += 1

        return used_rooms
