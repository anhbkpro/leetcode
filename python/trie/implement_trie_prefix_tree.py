from collections import defaultdict


class TrieNodeArray:
    def __init__(self):
        # Initialize links array and is_end flag
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord("a")] is not None

    def get(self, ch: str):
        return self.links[ord(ch) - ord("a")]

    def put(self, ch: str, node) -> None:
        self.links[ord(ch) - ord("a")] = node

    def set_end(self) -> None:
        self.is_end = True

    def is_end(self) -> bool:
        return self.is_end


class TrieArray:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNodeArray()
        self.call_count = 0

    def _validate_input(self, word: str) -> None:
        """
        Validate input constraints:
        1. 1 <= word.length <= 2000
        2. word consists only of lowercase English letters
        3. At most 3 * 10^4 calls in total
        """
        if not 0 <= len(word) <= 2000:
            raise ValueError("Word length must be between 0 and 2000")
        if not all(c.islower() for c in word):
            raise ValueError("Word must consist only of lowercase English letters")
        self.call_count += 1
        if self.call_count > 3 * 10**4:
            raise ValueError("Exceeded maximum number of calls (3 * 10^4)")

    def insert(self, word: str) -> None:
        self._validate_input(word)
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNodeArray())
            node = node.get(ch)
        node.set_end()

    def _search_prefix(self, word: str) -> TrieNodeArray:
        self._validate_input(word)
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self._search_prefix(prefix)
        return node is not None


class TrieNodeHash:
    def __init__(self):
        self.is_word = False
        self.links = defaultdict(TrieNodeHash)

    def get(self, ch: str):
        if ch in self.links:
            return self.links[ch]
        return None

    def put(self, ch: str, node) -> None:
        self.links[ch] = node

    def contains_key(self, ch: str) -> bool:
        return ch in self.links

    def set_end(self):
        self.is_word = True

    def is_end(self):
        return self.is_word


class TrieHash:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = TrieNodeHash()
        self.call_count = 0

    def _validate_input(self, word: str) -> None:
        """
        Validate input constraints:
        1. 1 <= word.length <= 2000
        2. word consists only of lowercase English letters
        3. At most 3 * 10^4 calls in total
        """
        if not 0 <= len(word) <= 2000:
            raise ValueError("Word length must be between 0 and 2000")
        if not all(c.islower() for c in word):
            raise ValueError("Word must consist only of lowercase English letters")
        self.call_count += 1
        if self.call_count > 3 * 10**4:
            raise ValueError("Exceeded maximum number of calls (3 * 10^4)")

    def insert(self, word: str) -> None:
        self._validate_input(word)
        node = self.head
        for c in word:
            if not node.contains_key(c):
                node.put(c, TrieNodeHash())
            node = node.get(c)
        node.set_end()

    def search(self, word: str) -> bool:
        self._validate_input(word)
        node = self.head
        for c in word:
            if not node.contains_key(c):
                return False
            node = node.get(c)
        return node and node.is_word

    def starts_with(self, prefix: str) -> bool:
        self._validate_input(prefix)
        node = self.head
        for c in prefix:
            if not node.contains_key(c):
                return False
            node = node.get(c)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.starts_with(prefix)
