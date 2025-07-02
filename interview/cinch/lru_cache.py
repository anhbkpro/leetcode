class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node mapping

        # Create dummy head and tail nodes for easier manipulation
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to head (most recently used)
            self._remove_node(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            # Move to head (most recently used)
            self._remove_node(node)
            self._add_to_head(node)
        else:
            # Add new key-value pair
            new_node = Node(key, value)

            if len(self.cache) >= self.capacity:
                # Remove least recently used (tail's previous)
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

            # Add new node to head
            self._add_to_head(new_node)
            self.cache[key] = new_node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        """Add a node right after the head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


# Test the implementation
if __name__ == "__main__":
    # Example 1
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))    # returns 1
    lru.put(3, 3)        # evicts key 2
    print(lru.get(2))    # returns -1 (not found)
    lru.put(4, 4)        # evicts key 1
    print(lru.get(1))    # returns -1 (not found)
    print(lru.get(3))    # returns 3
    print(lru.get(4))    # returns 4

    print("\n" + "="*50 + "\n")

    # Example 2 - More comprehensive test
    lru2 = LRUCache(3)
    lru2.put(1, 10)
    lru2.put(2, 20)
    lru2.put(3, 30)
    print(f"get(2): {lru2.get(2)}")    # 20, moves 2 to front
    lru2.put(4, 40)                    # evicts 1 (least recently used)
    print(f"get(1): {lru2.get(1)}")    # -1 (evicted)
    print(f"get(3): {lru2.get(3)}")    # 30
    print(f"get(2): {lru2.get(2)}")    # 20
    print(f"get(4): {lru2.get(4)}")    # 40
