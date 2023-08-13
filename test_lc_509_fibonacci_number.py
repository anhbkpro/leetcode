from lc_509_fibonacci_number import Solution


def test_fib():
    assert Solution.fib(0) == 0
    assert Solution.fib(1) == 1
    assert Solution.fib(2) == 1
    assert Solution.fib(3) == 2
    assert Solution.fib(4) == 3
    assert Solution.fib(5) == 5
    assert Solution.fib(6) == 8
    assert Solution.fib(7) == 13
