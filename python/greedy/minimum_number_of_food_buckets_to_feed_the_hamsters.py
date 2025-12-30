class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        if "HHH" in hamsters:
            return -1

        count = hamsters.count("H")
        if (
            len(hamsters) == count
            or hamsters.startswith("HH")
            or hamsters.endswith("HH")
        ):
            return -1

        count_diff_1 = hamsters.count("H.H")
        if not count_diff_1:
            return count

        return count - count_diff_1
