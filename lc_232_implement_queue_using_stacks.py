class MyQueue:

    def __init__(self):
        self.s1 = []  # inverse of the queue, at -1 index (last index of array) is the front item for the queue; at 0
        # index is the back of the queue
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())  # temporally move all current items in s1 to s2
        self.s1.append(x)  # insert x as the first element of s1
        while self.s2:
            self.s1.append(self.s2.pop())  # then move all items from s2 back to s1

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()