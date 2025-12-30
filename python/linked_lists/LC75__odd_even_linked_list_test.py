from linked_lists.LC75__odd_even_linked_list import ListNode, Solution


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
    assert solution.oddEvenList(None) is None


def test_single_node():
    solution = Solution()
    head = ListNode(1)
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1]


def test_two_nodes():
    solution = Solution()
    head = create_linked_list([1, 2])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 2]


def test_odd_length():
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 5, 2, 4]


def test_even_length():
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 2, 4]


def test_larger_list():
    solution = Solution()
    head = create_linked_list([2, 1, 3, 5, 6, 4, 7])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [2, 3, 6, 7, 1, 5, 4]
