from lc_378_kth_smallest_element_in_a_sorted_matrix import Solution


def test_kth_smallest():
    assert (
            Solution.kth_smallest(
                matrix=[[1, 5, 9],
                        [10, 11, 13],
                        [12, 13, 15]],
                k=8
            ) == 13
    )
