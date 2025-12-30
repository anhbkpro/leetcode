from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    pairs = [[k, v] for k, v in cnt.items()]
    pairs.sort(key=lambda x: (-x[1], -x[0]))
    pairs = pairs[:k]
    return [x[0] for x in pairs]
