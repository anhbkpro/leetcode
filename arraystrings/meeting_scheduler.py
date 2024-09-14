from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        def is_intersected(range1, range2: List[int]) -> bool:
            start1, end1 = range1
            start2, end2 = range2
            return max(start1, start2) <= min(end1, end2)

        slots1.sort()
        slots2.sort()
        ans = []
        while len(slots1) > 0 and len(slots2) > 0:
            first = slots1[0]
            second = slots2[0]
            if is_intersected(first, second):
                s = max(first[0], second[0])
                e = min(first[1], second[1])
                if e - s >= duration:
                    return [s, s + duration]
            if second[1] < first[1]:
                slots2.pop(0)
            else:
                slots1.pop(0)

        return ans
