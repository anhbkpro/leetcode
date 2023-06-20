from typing import List


def getAverages(nums: List[int], k: int) -> List[int]:
    # When a single element is considered then its average will be the number itself only.
    if k == 0:
        return nums

    n = len(nums)
    averages = [-1] * n

    # Any index will not have 'k' elements in it's left and right.
    if 2 * k + 1 > n:
        return averages

    # Generate 'prefix' array for 'nums'.
    # 'prefix[i + 1]' will be sum of all elements of 'nums' from index '0' to 'i'.
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # We iterate only on those indices which have at least 'k' elements in their left and right.
    # i.e. indices from 'k' to 'n - k'.
    for i in range(k, n - k):
        left_bound, right_bound = i - k, i + k
        sub_array_sum = prefix[right_bound + 1] - prefix[left_bound]
        average = sub_array_sum // (2 * k + 1)
        averages[i] = average

    return averages


class Solution:
    pass
