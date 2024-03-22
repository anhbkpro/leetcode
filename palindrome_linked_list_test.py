from palindrome_linked_list import ListNode, Solution


def test_isPalindrome():
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    result = s.isPalindrome(head)
    assert result is True
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    result = s.isPalindrome(head)
    assert result is True
    head = ListNode(1, ListNode(2))
    result = s.isPalindrome(head)
    assert result is False
