# 901. Online Stock Span (monotonic decreasing stack)
from typing import List, Tuple


class StockSpanner:

    def __init__(self) -> None:
        """Initialize the StockSpanner with a monotonic decreasing stack."""
        self.current_index: int = 0
        self.stack: List[Tuple[float, int]] = [(float("inf"), 0)]

    def next(self, price: int) -> int:
        """Return the stock span for the given price."""
        self.current_index += 1
        self._pop_while_less_equal(price)
        self.stack.append((price, self.current_index))
        return self.current_index - self.stack[-2][1]

    def _pop_while_less_equal(self, price: int) -> None:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
