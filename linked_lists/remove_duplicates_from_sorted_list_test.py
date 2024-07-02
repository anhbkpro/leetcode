from .remove_duplicates_from_sorted_list import Solution
from .linked_list_node import ListNode


def test_remove_duplicates_from_sorted_list():
    # head = [1,1,2]
    # Output: [1,2]
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    ans = Solution().deleteDuplicates(head)
    assert ans.val == 1
    assert ans.next.val == 2
