from lc_61_rotate_list import ListNode


class Solution:
    @staticmethod
    def plus_one(head: ListNode) -> ListNode:
        """
        Given a non-negative integer represented as a linked list of digits, plus one to the integer.
        The digits are stored such that the most significant digit is at the head of the list.
        :param head: head of the linked list
        :return: head of the new linked list
        """
        # sentinel head to handle edge case of 999 -> 1000 (add 1 more node to the head)
        sentinel = ListNode(0)
        sentinel.next = head
        not_nine = sentinel

        # find the rightmost not-nine node value
        # for example, if input is 192999, not_nine will be 2
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
