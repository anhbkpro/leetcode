import collections
from typing import List


def countElements(arr: List[int]) -> int:
    counter = collections.Counter(arr)
    print(counter)
    ans = 0
    for item in arr:
        if item + 1 in counter:
            ans += 1
    return ans


class Solution:
    pass
