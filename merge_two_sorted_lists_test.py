from merge_two_sorted_lists import Solution, LinkedList


def test_mergeTwoLists():
    s = Solution()
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l2 = LinkedList()
    l2.append(1)
    l2.append(3)
    l2.append(4)
    result = s.mergeTwoLists(l1.head, l2.head)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next.val == 4
    assert result.next.next.next.next.next.val == 4
    assert result.next.next.next.next.next.next is None
    l1 = LinkedList()
    l1.append(1)
    l2 = LinkedList()
    l2.append(1)
    l2.append(2)
    l2.append(3)
    result = s.mergeTwoLists(l1.head, l2.head)
    assert result.val == 1
    assert result.next.val == 1
    assert result.next.next.val == 2
    assert result.next.next.next.val == 3
    assert result.next.next.next.next is None
    l1 = LinkedList()
    l1.append(1)
    l2 = LinkedList()
    l2.append(2)
    l2.append(3)
    result = s.mergeTwoLists(l1.head, l2.head)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next is None
    l1 = LinkedList()
    l1.append(1)
    l2 = LinkedList()
    l2.append(2)
    l2.append(3)
    l2.append(4)
    result = s.mergeTwoLists(l1.head, l2.head)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 4
    assert result.next.next.next.next is None
