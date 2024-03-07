from lc_2095_delete_the_middle_node_of_a_linked_list import ListNode, Solution

data = [1, 3, 4, 7, 1, 2, 6]
head = ListNode(val=data[0])
current = head
for i in range(1, len(data)):
    current.next = ListNode(val=data[i])
    current = current.next


def test_delete_middle():
    result = Solution.deleteMiddle(head=head)
    result_str = ""
    while result:
        result_str += str(result.val)
        result = result.next

    assert result_str == "134126"
