from typing import List


def anagramMappings(nums1: List[int], nums2: List[int]) -> List[int]:
    hash_map = {}
    ans = []
    for i in range(len(nums2)):
        hash_map[nums2[i]] = i

    for i in range(len(nums1)):
        ans.append(hash_map[nums1[i]])

    return ans


class Solution:
    pass
