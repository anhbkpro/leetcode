from typing import List
import collections


class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        my_trie = self.trie
        for char in word:
            if char not in my_trie.children:
                my_trie.children[char] = TrieNode()
            my_trie = my_trie.children[char]

        my_trie.count += 1

    def search(self, word: str) -> int:
        curr = self.trie
        for char in word:
            if char not in curr.children:
                return 0
            curr = curr.children[char]

        return curr.count


def equalPairs(grid: List[List[int]]) -> int:
    trie = Trie()
    count = 0
    n = len(grid)

    # Add up the frequency of each column in map.
    for c in range(n):
        col = [grid[i][c] for i in range(n)]
        trie.insert(str(col))

    # Add up the frequency of each row in map.
    for r in range(n):
        row = grid[r]
        count += trie.search(str(row))

    return count


class Solution:
    pass
