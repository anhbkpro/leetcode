import heapq
from typing import List


class Solution:
    @staticmethod
    def most_booked(n: int, meetings: List[List[int]]) -> int:
        meeting_count = [0] * n
        available_rooms, allocated_rooms = list(range(n)), []
        heapq.heapify(available_rooms)
        for start, end in sorted(meetings):
            while allocated_rooms and allocated_rooms[0][0] <= start:
                # the meeting at the top of the min-heap has ended, free the room
                _, room = heapq.heappop(allocated_rooms)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                # there are rooms available, allocate the room with the lowest number for meeting
                room = heapq.heappop(available_rooms)
                # allocate this meeting to `taken_room`
                heapq.heappush(allocated_rooms, (end, room))
            else:
                # if all rooms are taken, we need to wait until a room free (which is the room has the smallest end, top of the min-heap)
                free_at, room = heapq.heappop(allocated_rooms)
                heapq.heappush(allocated_rooms, (end + (free_at - start), room))
            meeting_count[room] += 1

        return meeting_count.index(max(meeting_count))
