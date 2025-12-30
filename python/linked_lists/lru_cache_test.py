import pytest

from .lru_cache import LRUCache


@pytest.fixture
def cache():
    return LRUCache(2)  # Most test cases use capacity of 2


def test_basic_operations(cache):
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)
    assert cache.get(2) == 2
    assert cache.get(1) == 1


def test_capacity_limit():
    cache = LRUCache(1)  # Cache with capacity 1
    cache.put(1, 1)
    cache.put(2, 2)  # This should evict key 1
    assert cache.get(1) == -1  # Key 1 should be evicted
    assert cache.get(2) == 2  # Key 2 should be present


def test_lru_eviction():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Accessing 1 makes it most recently used
    cache.put(3, 3)  # This should evict key 2
    assert cache.get(2) == -1  # Key 2 should be evicted
    assert cache.get(1) == 1  # Key 1 should still be present
    assert cache.get(3) == 3  # Key 3 should be present


def test_update_existing_key():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # Update value of key 1
    assert cache.get(1) == 10  # Should return updated value
    assert cache.get(2) == 2  # Key 2 should still be present


def test_large_capacity():
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)  # Should evict key 1
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_mixed_operations():
    cache = LRUCache(2)
    assert cache.get(1) == -1  # Get non-existent key
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # Evicts key 2
    assert cache.get(2) == -1
    cache.put(4, 4)  # Evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_repeated_operations():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    cache.put(3, 3)  # Should evict 1 since it was accessed before 2
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3


def test_update_makes_most_recent():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 1)  # Update makes 1 most recent
    cache.put(3, 3)  # Should evict 2
    assert cache.get(1) == 1
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_get_updates_order():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # Makes 1 most recent
    cache.put(3, 3)  # Should evict 2
    assert cache.get(1) == 1
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_zero_capacity():
    cache = LRUCache(0)
    cache.put(1, 1)
    assert cache.get(1) == -1


def test_single_key_repeated_update():
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(1, 2)
    cache.put(1, 3)
    assert cache.get(1) == 3


def test_eviction_order():
    cache = LRUCache(3)
    cache.put(1, 1)  # [1]
    cache.put(2, 2)  # [1, 2]
    cache.put(3, 3)  # [1, 2, 3]
    assert cache.get(1) == 1  # [2, 3, 1]
    cache.put(4, 4)  # [3, 1, 4], evicts 2
    assert cache.get(2) == -1
    assert cache.get(3) == 3  # [1, 4, 3]
    cache.put(5, 5)  # [4, 3, 5], evicts 1
    assert cache.get(1) == -1
    assert cache.get(4) == 4
    assert cache.get(3) == 3
    assert cache.get(5) == 5
