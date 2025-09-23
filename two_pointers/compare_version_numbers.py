class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        diff = abs(len(nums1) - len(nums2))
        while diff > 0:
            diff -= 1
            if len(nums1) > len(nums2):
                nums2.append("0")
            else:
                nums1.append("0")

        for v1, v2 in zip(nums1, nums2):
            num1 = int(v1)
            num2 = int(v2)
            if num1 == num2:
                continue

            if num1 < num2:
                return -1

            return 1

        return 0
