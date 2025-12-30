import pytest

from .implement_trie_prefix_tree import TrieArray, TrieHash


@pytest.fixture
def trie_hash():
    return TrieHash()


@pytest.fixture
def trie_array():
    return TrieArray()


class TestTrieHash:
    def test_insert_and_search(self, trie_hash):
        trie_hash.insert("apple")
        assert trie_hash.search("apple") is True
        assert trie_hash.search("app") is False

    def test_starts_with(self, trie_hash):
        trie_hash.insert("apple")
        assert trie_hash.starts_with("app") is True
        assert trie_hash.starts_with("apt") is False

    def test_empty_string(self, trie_hash):
        trie_hash.insert("")
        assert trie_hash.search("") is True
        assert trie_hash.starts_with("") is True

    def test_multiple_words(self, trie_hash):
        words = ["hello", "world", "hell", "word", "he"]
        for word in words:
            trie_hash.insert(word)

        for word in words:
            assert trie_hash.search(word) is True

        assert trie_hash.search("help") is False
        assert trie_hash.starts_with("he") is True
        assert trie_hash.starts_with("wor") is True

    def test_word_length_constraint(self, trie_hash):
        # Test word length > 2000
        long_word = "a" * 2001
        with pytest.raises(ValueError, match="Word length must be between 0 and 2000"):
            trie_hash.insert(long_word)

    def test_lowercase_constraint(self, trie_hash):
        # Test non-lowercase word
        with pytest.raises(
            ValueError, match="Word must consist only of lowercase English letters"
        ):
            trie_hash.insert("Apple")

    def test_call_limit_constraint(self, trie_hash):
        # Test call limit > 3 * 10^4
        with pytest.raises(ValueError, match="Exceeded maximum number of calls"):
            for i in range(30001):
                trie_hash.insert("a")


class TestTrieArray:
    def test_insert_and_search(self, trie_array):
        trie_array.insert("apple")
        assert trie_array.search("apple") is True
        assert trie_array.search("app") is False

    def test_starts_with(self, trie_array):
        trie_array.insert("apple")
        assert trie_array.starts_with("app") is True
        assert trie_array.starts_with("apt") is False

    def test_empty_string(self, trie_array):
        trie_array.insert("")
        assert trie_array.search("") is True
        assert trie_array.starts_with("") is True

    def test_multiple_words(self, trie_array):
        words = ["hello", "world", "hell", "word", "he"]
        for word in words:
            trie_array.insert(word)

        for word in words:
            assert trie_array.search(word) is True

        assert trie_array.search("help") is False
        assert trie_array.starts_with("he") is True
        assert trie_array.starts_with("wor") is True

    def test_word_length_constraint(self, trie_array):
        # Test word length > 2000
        long_word = "a" * 2001
        with pytest.raises(ValueError, match="Word length must be between 0 and 2000"):
            trie_array.insert(long_word)

    def test_lowercase_constraint(self, trie_array):
        # Test non-lowercase word
        with pytest.raises(
            ValueError, match="Word must consist only of lowercase English letters"
        ):
            trie_array.insert("Apple")

    def test_call_limit_constraint(self, trie_array):
        # Test call limit > 3 * 10^4
        with pytest.raises(ValueError, match="Exceeded maximum number of calls"):
            for i in range(30001):
                trie_array.insert("a")
