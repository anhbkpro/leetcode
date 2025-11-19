from linked_lists.LC75__reverse_linked_list import Solution, ListNode


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def test_empty_list():
    solution = Solution()
    assert solution.reverseList(None) is None


def test_single_node():
    solution = Solution()
    head = ListNode(1)
    result = solution.reverseList(head)
    assert linked_list_to_list(result) == [1]


def test_two_nodes():
    solution = Solution()
    head = create_linked_list([1, 2])
    result = solution.reverseList(head)
    assert linked_list_to_list(result) == [2, 1]


def test_three_nodes():
    solution = Solution()
    head = create_linked_list([1, 2, 3])
    result = solution.reverseList(head)
    assert linked_list_to_list(result) == [3, 2, 1]


def test_four_nodes():
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4])
    result = solution.reverseList(head)
    assert linked_list_to_list(result) == [4, 3, 2, 1]


def test_negative_values():
    solution = Solution()
    head = create_linked_list([-1, -2, -3])
    result = solution.reverseList(head)
    assert linked_list_to_list(result) == [-3, -2, -1]


def test_mixed_values():
    solution = Solution()
    head = create_linked_list([1, -2, 3, -4])
    result = solution.reverseList(head)
    assert linked_list_to_list(result) == [-4, 3, -2, 1]
