from lc_1155_number_of_dice_rolls_with_target_sum import Solution


def test_num_rolls_to_target():
    assert Solution().numRollsToTarget(n=1, k=6, target=3) == 1
    assert Solution().numRollsToTarget(n=2, k=6, target=7) == 6
