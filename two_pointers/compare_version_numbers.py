import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        diff = abs(len(nums1) - len(nums2))
        while diff > 0:
            logger.info(f"Padding shorter version: {nums1} and {nums2}")
            diff -= 1
            if len(nums1) > len(nums2):
                logger.info(f"Padding {nums2} with 0")
                nums2.append("0")
            else:
                logger.info(f"Padding {nums1} with 0")
                nums1.append("0")

        logger.info(f"Normalized versions: {nums1} and {nums2}")
        for v1, v2 in zip(nums1, nums2):
            num1 = int(v1)
            num2 = int(v2)
            logger.info(f"Comparing numbers: {num1} and {num2}")
            if num1 == num2:
                continue

            if num1 < num2:
                return -1

            return 1

        return 0
