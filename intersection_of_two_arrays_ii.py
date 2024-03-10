from collections import Counter


class Solution:
    def intersection(self, nums1, nums2):
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []
        for num in counter1:
            if num in counter2:
                result += [num] * min(counter1[num], counter2[num])

        return result
