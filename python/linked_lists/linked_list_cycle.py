class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionHashTable:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        current = head
        while current is not None:
            if current in nodes_seen:
                return True
            nodes_seen.add(current)
            current = current.next
        return False


class SolutionFloydCycle:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
