from .insert_greatest_common_divisors_in_linked_list import ListNode, Solution


def test_insert_greatest_common_divisors():
    # Input: head = [7]
    # Output: [7]
    head = ListNode(7)
    assert Solution().insertGreatestCommonDivisors(head) == head
    # Input: head = [18,6,10,3]
    # Output: [18,6,6,2,10,1,3]
    head = ListNode(18)
    head.next = ListNode(6)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(3)
    ans = Solution().insertGreatestCommonDivisors(head)
    assert ans.val == 18
    assert ans.next.val == 6
    assert ans.next.next.val == 6
    assert ans.next.next.next.val == 2
    assert ans.next.next.next.next.val == 10
    assert ans.next.next.next.next.next.val == 1
    assert ans.next.next.next.next.next.next.val == 3
