from lc_225_implement_stack_using_queues import MyStack


def test_my_stack():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() is False
