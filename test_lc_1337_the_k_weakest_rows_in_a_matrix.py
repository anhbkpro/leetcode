from lc_1337_the_k_weakest_rows_in_a_matrix import Solution


def test_k_weakest_rows():
    assert (
        Solution.kWeakestRows(
            mat=[
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ], k=3) == [2, 0, 3]
    )
