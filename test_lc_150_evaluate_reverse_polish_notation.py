from lc_150_evaluate_reverse_polish_notation import Solution


def test_eval_rpn():
    assert Solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
