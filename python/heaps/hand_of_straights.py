import heapq
from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = Counter(hand)
        n = len(hand)
        if n % groupSize != 0:
            return False

        heap = []
        for num in hand:
            heapq.heappush(heap, num)

        while len(heap) > 0:
            num = heapq.heappop(heap)
            freq = c[num]
            if freq == 0:
                continue

            c[num] -= freq
            for i in range(1, groupSize):
                if c[num + i] < freq:
                    return False

                c[num + i] -= freq
                if c[num + i] == 0:
                    del c[num + i]

        return True
