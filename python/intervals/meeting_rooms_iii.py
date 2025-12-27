from heapq import heapify, heappop, heappush
from math import inf
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heappop(used_rooms)
                heappush(used_rooms, [room_availability_time + end - start, room])
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))

    def mostBookedSortingAndCounting(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_time_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability_time[i] <= start:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability_time[i] = end
                    break
                if min_room_availability_time > room_availability_time[i]:
                    min_room_availability_time = room_availability_time[i]
                    min_available_time_room = i
            if not found_unused_room:
                room_availability_time[min_available_time_room] += end - start
                meeting_count[min_available_time_room] += 1

        return meeting_count.index(max(meeting_count))
