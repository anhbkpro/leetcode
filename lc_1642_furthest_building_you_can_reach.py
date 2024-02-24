import heapq
from typing import List


class Solution:
    @staticmethod
    def furthest_building(heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []  # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue

            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            print(ladder_allocations)

            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue

            # Otherwise, we will need to take a climb out of ladder_allocations
            print(f"we have {bricks} remaining bricks")
            # in order to get further, we'll need to use bricks for the smallest climb we've seen so far (i.e. the top of the heap)
            bricks -= heapq.heappop(
                ladder_allocations
            )  # We'll use the smallest climb we've seen so far.
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                print(f"--- which is not enough to climb up from {i} building")
                return i

        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1
