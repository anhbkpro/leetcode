class DDL:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = DDL(homepage)

    def visit(self, url: str) -> None:
        self.head.next = DDL(url, self.head)
        self.head = self.head.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.head.prev is not None:
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.head.next is not None:
            self.head = self.head.next
            steps -= 1
        return self.head.val
