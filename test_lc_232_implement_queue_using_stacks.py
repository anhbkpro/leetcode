from lc_232_implement_queue_using_stacks import MyQueue


def test_implement_queue_using_stacks():
    queue = MyQueue()
    queue.push(1)  # queue is: [1]
    queue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    assert queue.peek() == 1  # return 1
    assert queue.pop() == 1  # return 1, queue is [2]
    assert queue.empty() is False  # return false

