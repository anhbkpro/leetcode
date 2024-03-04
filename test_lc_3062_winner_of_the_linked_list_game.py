from lc_3062_winner_of_the_linked_list_game import ListNode, Solution


def test_game_result():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    assert Solution.game_result(head) == "Odd"
    head = ListNode(1, ListNode(2, ListNode(4, ListNode(3))))
    assert Solution.game_result(head) == "Tie"
    head = ListNode(2, ListNode(1))
    assert Solution.game_result(head) == "Even"
