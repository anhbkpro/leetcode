from typing import List, Tuple


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        def find_intersection(
            slot1: Tuple[int, int], slot2: Tuple[int, int]
        ) -> Tuple[int, int]:
            start = max(slot1[0], slot2[0])
            end = min(slot1[1], slot2[1])
            return (start, end) if start < end else None

        # Sort slots and convert to iterator for efficient popping
        slots1 = iter(sorted(slots1))
        slots2 = iter(sorted(slots2))

        try:
            slot1 = next(slots1)
            slot2 = next(slots2)

            while True:
                intersection = find_intersection(slot1, slot2)
                if intersection:
                    start, end = intersection
                    if end - start >= duration:
                        return [start, start + duration]

                # Move the pointer of the slot that ends earlier
                if slot1[1] < slot2[1]:
                    slot1 = next(slots1)
                else:
                    slot2 = next(slots2)

        except StopIteration:
            # One or both of the slot lists have been exhausted
            pass

        return []
