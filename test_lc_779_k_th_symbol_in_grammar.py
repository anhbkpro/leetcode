from lc_779_k_th_symbol_in_grammar import Solution

solution = Solution()


def test_kth_grammar():
    assert solution.kthGrammar(1, 1) == 0
    assert solution.kthGrammar(2, 1) == 0
    assert solution.kthGrammar(2, 2) == 1
