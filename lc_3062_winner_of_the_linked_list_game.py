# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def game_result(head: Optional[ListNode]) -> str:
        scores = [0, 0]
        while head and head.next:
            winner = 0 if head.val > head.next.val else 1
            scores[winner] += 1
            head = head.next.next

        if scores[0] == scores[1]:
            return "Tie"

        return "Even" if scores[0] > scores[1] else "Odd"
