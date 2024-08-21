from .strange_printer import Solution


def test_strange_printer():
    assert Solution().strangePrinter("aaabbb") == 2
    assert Solution().strangePrinter("aba") == 2
