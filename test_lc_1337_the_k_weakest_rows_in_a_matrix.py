from lc_1337_the_k_weakest_rows_in_a_matrix import Solution


def test_k_weakest_rows():
    assert (
            Solution.k_weakest_rows(
                mat=[[1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1]],
                k=3
            ) == [2, 0, 3]
    )


def test_k_weakest_rows_nsmallest():
    assert (
            Solution.k_weakest_rows_nsmallest(
                mat=[[1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1]],
                k=3
            ) == [2, 0, 3]
    )
