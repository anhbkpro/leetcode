import heapq
from typing import List


def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    # sort pair (nums1[i], nums2[i]) by nums2[i] in descending order
    pairs = [(a, b) for a, b in zip(nums1, nums2)]
    pairs.sort(key=lambda x: -x[1])

    # Use a min-heap to maintain the top k elements.
    top_k_heap = [x[0] for x in pairs[:k]]
    top_k_sum = sum(top_k_heap)
    heapq.heapify(top_k_heap)

    # The score of the first k pairs.
    answer = top_k_sum * pairs[k - 1][1]

    # Iterate over every nums2[i] as minimum from nums2.
    for i in range(k, len(nums1)):
        top_k_sum -= heapq.heappushpop(top_k_heap, pairs[i][0])  # pop the smallest element and push pairs[i][0]

        # above line of code is equivalent 3 following lines:
        # top_k_sum -= heapq.heappop(top_k_heap)
        # top_k_sum += pairs[i][0]
        # heapq.heappush(top_k_heap, pairs[i][0])

        # Update answer as the maximum score.
        answer = max(answer, top_k_sum * pairs[i][1])

    return answer


class Solution:
    pass
