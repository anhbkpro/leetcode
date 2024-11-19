from .design_a_stack_with_increment_operation import CustomStack


def test_design_a_stack_with_increment_operation():
    stk = CustomStack(3)
    assert stk.push(1) is None
    assert stk.push(2) is None
    assert stk.pop() == 2
    assert stk.push(2) is None
    assert stk.push(3) is None
    assert stk.push(4) is None
    assert stk.increment(5, 100) is None
    assert stk.increment(2, 100) is None
    assert stk.pop() == 103
    assert stk.pop() == 202
