from typing import List


def max_distance(arrays: List[List[int]]) -> int:
    arrays.sort(key=lambda x: x[-1])
    answer = 0
    for arr in arrays[:-1]:
        answer = max(answer, abs(arr[0] - arrays[-1][-1]))
        answer = max(answer, abs(arr[-1] - arrays[-1][0]))

    return answer


class Solution:
    pass
