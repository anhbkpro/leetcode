from .implement_trie_prefix_tree  import Trie


def test_trie():
    obj = Trie()
    obj.insert("apple")
    assert obj.search("apple") is True
    assert obj.search("app") is False
    assert obj.starts_with("app") is True
