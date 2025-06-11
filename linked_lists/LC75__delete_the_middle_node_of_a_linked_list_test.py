from linked_lists.LC75__delete_the_middle_node_of_a_linked_list import (
    Solution,
    ListNode,
)


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


def test_single_node():
    solution = Solution()
    head = ListNode(1)
    assert solution.deleteMiddle(head) is None


def test_two_nodes():
    solution = Solution()
    head = create_linked_list([1, 2])
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == [1]


def test_odd_length():
    solution = Solution()
    head = create_linked_list([1, 3, 4, 7, 1, 2, 6])
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == [1, 3, 4, 1, 2, 6]


def test_even_length():
    solution = Solution()
    head = create_linked_list([1, 2, 3, 4])
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == [1, 2, 4]
