from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for ticket in tickets:
            ans += min(ticket, tickets[k])
        start = k + 1
        while start < len(tickets):
            if tickets[start] >= tickets[k]:
                ans -= 1
            start += 1
        return ans
