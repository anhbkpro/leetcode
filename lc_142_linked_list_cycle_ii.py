from typing import Optional

from lc_141_linked_list_cycle import ListNode


class Solution:
    @staticmethod
    def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize an empty hash set
        nodes_seen = set()

        # Start from the head of the linked list
        node = head
        while node is not None:
            # If the current node is in nodes_seen, we have a cycle
            if node in nodes_seen:
                return node
            else:
                # Add this node to nodes_seen and move to the next node
                nodes_seen.add(node)
                node = node.next

        # If we reach a null node, there is no cycle
        return None

    @staticmethod
    def detect_cycle_tortoise_and_hare(head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize tortoise and hare pointers
        tortoise = head
        hare = head

        # Move tortoise one step and hare two steps
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next

            # Check if the hare meets the tortoise
            if tortoise == hare:
                break

        # Check if there is no cycle
        if not hare or not hare.next:
            return None

        # Reset either tortoise or hare pointer to the head
        hare = head

        # Move both pointers one step until they meet again
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        # Return the node where the cycle begins
        return tortoise
