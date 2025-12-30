from collections import defaultdict

from sortedcontainers import SortedSet


class NumberContainers:
    def __init__(self):
        self.number_to_indices = defaultdict(SortedSet)
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            prev_number = self.index_to_number[index]
            self.number_to_indices[prev_number].remove(index)
            if not self.number_to_indices[prev_number]:
                del self.number_to_indices[prev_number]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices:
            return -1
        return self.number_to_indices[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
