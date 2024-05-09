from heaps.maximize_happiness_of_selected_children import Solution


def test_maximize_happiness_of_selected_children():
    assert Solution().maximumHappinessSum(happiness = [1,2,3], k = 2) == 4
    assert Solution().maximumHappinessSum(happiness = [1,1,1,1], k = 2) == 1
    assert Solution().maximumHappinessSum(happiness = [2,3,4,5], k = 1) == 5
