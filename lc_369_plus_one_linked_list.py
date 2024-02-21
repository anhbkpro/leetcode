from lc_61_rotate_list import ListNode


class Solution:
    @staticmethod
    def plus_one(head: ListNode) -> ListNode:
        # sentinel head to handle edge case of 999 -> 1000 (add 1 more node to the head)
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine node value
        # for example, if input is 1929, not_nine will be 2
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine node value by 1
        not_nine.val += 1
        not_nine = not_nine.next

        # set all the following nines to zeros (for example, 192999 -> 193000)
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next

        return sentinel if sentinel.val else sentinel.next
