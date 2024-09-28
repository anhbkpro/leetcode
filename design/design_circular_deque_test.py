from .design_circular_deque import MyCircularDeque


def test_design_circular_deque():
    myCircularDeque = MyCircularDeque(3)
    assert myCircularDeque.insertLast(1) == True
    assert myCircularDeque.insertLast(2) == True
    assert myCircularDeque.insertFront(3) == True
    assert myCircularDeque.insertFront(4) == False
    assert myCircularDeque.getRear() == 2
    assert myCircularDeque.isFull() == True
    assert myCircularDeque.deleteLast() == True
    assert myCircularDeque.insertFront(4) == True
    assert myCircularDeque.getFront() == 4
