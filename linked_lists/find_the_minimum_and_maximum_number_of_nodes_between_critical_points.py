from typing import Optional, List
from .linked_list_node import LinkedListNode


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[LinkedListNode]) -> List[int]:
        ans = []
        index = 0
        while head:
            if self.isCriticalPoint(head):
                ans.append(index + 1)
            head = head.next
            index += 1

        if len(ans) < 2:
            return [-1, -1]

        maxDistance = ans[-1] - ans[0]
        minDistance = ans[1] - ans[0]
        for i in range(1, len(ans)):
            minDistance = min(minDistance, ans[i] - ans[i-1])

        return [minDistance, maxDistance]

    def isCriticalPoint(self, head: Optional[LinkedListNode]) -> bool:
        if head is None:
            return False
        if head.next is None or head.next.next is None:
            return False
        if head.val > head.next.val and head.next.next.val > head.next.val:
            return True
        if head.val < head.next.val and head.next.next.val < head.next.val:
            return True
        return False



