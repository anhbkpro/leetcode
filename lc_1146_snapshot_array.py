class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[(0, 0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history_records[index].append((self.id, val))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        # shorter version
        # snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
        # return self.history_records[index][snap_index - 1][1]
        history = self.history_records[index]
        left, right = 0, len(history) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if history[mid][0] <= snap_id:
                left = mid
            else:
                right = mid - 1
        return history[left][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
