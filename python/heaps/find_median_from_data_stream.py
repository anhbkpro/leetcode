import heapq
from typing import List


class MedianFinder:
    """
    A class to find the median from a data stream using two heaps.
    The smaller half is stored in a max heap (small) and the larger half in a min heap (large).
    """

    def __init__(self) -> None:
        """
        Initialize the MedianFinder with two empty heaps:
        - max_heap: stores the smaller half (as negative numbers to simulate max heap)
        - min_heap: stores the larger half
        """
        self.max_heap: List[
            int
        ] = []  # stores smaller half (negated for max heap behavior)
        self.min_heap: List[int] = []  # stores larger half

    def _balance_heaps(self) -> None:
        """
        Balance the two heaps so their sizes differ by at most 1.
        The max_heap can have one more element than min_heap.
        """
        # If max_heap has more than one extra element, move one to min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        # If min_heap has more elements, move one to max_heap
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def addNum(self, num: int) -> None:
        """
        Add a number to the data stream and maintain heap balance.

        Args:
            num: The number to add to the data stream
        """
        # Add to appropriate heap based on value
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        # Ensure heaps remain balanced
        self._balance_heaps()

    def findMedian(self) -> float:
        """
        Find the median of the current data stream.

        Returns:
            float: The median value of all added numbers
        """
        if len(self.max_heap) > len(self.min_heap):
            # If max_heap has one more element, that's the median
            return -self.max_heap[0]
        else:
            # Otherwise, average of the two middle elements
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
