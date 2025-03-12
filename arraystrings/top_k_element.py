from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    cnt = Counter(nums)
    pairs = [[k, v] for k, v in cnt.items()]
    pairs.sort(key=lambda x: (-x[1], -x[0]))
    pairs = pairs[:k]
    return [x[0] for x in pairs]
