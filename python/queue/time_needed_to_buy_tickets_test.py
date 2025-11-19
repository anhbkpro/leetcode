from time_needed_to_buy_tickets import Solution


def test_time_needed_to_buy_tickets_test():
    s = Solution()
    assert s.timeRequiredToBuy(tickets=[2, 3, 2], k=2) == 6
    assert s.timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0) == 8
