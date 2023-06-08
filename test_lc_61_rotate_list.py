from lc_61_rotate_list import rotate_right, ListNode


def test_rotate_right():
    # Input: head = [1, 2, 3, 4, 5], k = 2
    # Output: [4, 5, 1, 2, 3]
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"node: {node}")
    result = f"{rotate_right(node, 2)}"
    assert result == "[4, 5, 1, 2, 3]"
