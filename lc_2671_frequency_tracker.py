from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.num = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq[self.num[number]] = max(0, self.freq[self.num[number]] - 1)
        self.num[number] += 1
        self.freq[self.num[number]] += 1

    def deleteOne(self, number: int) -> None:
        self.freq[self.num[number]] = max(0, self.freq[self.num[number]] - 1)
        self.num[number] = max(self.num[number] - 1, 0)
        self.freq[self.num[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] != 0
