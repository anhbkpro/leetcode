from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_devices = bank[0].count("1")
        for i in range(1, len(bank)):
            cur_devices = bank[i].count("1")
            if cur_devices == 0:
                continue
            ans += prev_devices * cur_devices
            prev_devices = cur_devices

        return ans
