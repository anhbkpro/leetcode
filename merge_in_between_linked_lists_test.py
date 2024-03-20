from merge_in_between_linked_lists import Solution, ListNode

# Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [10,1,13,1000000,1000001,1000002,9,5]
def test_merge_in_between():
    list1 = ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5))))))
    list2 = ListNode(1000000, ListNode(1000001, ListNode(1000002)))
    a = 3
    b = 4
    result = Solution().mergeInBetween(list1, a, b, list2)
    assert result.val == 10
    assert result.next.val == 1
    assert result.next.next.val == 13
    assert result.next.next.next.val == 1000000
    assert result.next.next.next.next.val == 1000001
    assert result.next.next.next.next.next.val == 1000002
    assert result.next.next.next.next.next.next.val == 5
