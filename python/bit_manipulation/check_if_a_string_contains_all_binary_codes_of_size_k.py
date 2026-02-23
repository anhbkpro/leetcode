class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        needed = 1 << k

        if n < k:
            return False

        seen = set()
        mask = 0

        for i in range(n):
            # shift left and add current bit
            mask = ((mask << 1) & (needed - 1)) | int(s[i])

            if i >= k - 1:
                seen.add(mask)
                print(mask)
                if len(seen) == needed:
                    return True

        return False
