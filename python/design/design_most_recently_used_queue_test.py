from design.design_most_recently_used_queue import MRUQueue


def test_initialization():
    # Test initialization with different sizes
    queue = MRUQueue(5)  # Initial: [1,2,3,4,5]
    assert queue.fetch(1) == 1  # After: [2,3,4,5,1]
    assert queue.fetch(1) == 2  # After: [3,4,5,1,2]
    assert queue.fetch(1) == 3  # After: [4,5,1,2,3]
    assert queue.fetch(1) == 4  # After: [5,1,2,3,4]
    assert queue.fetch(1) == 5  # After: [1,2,3,4,5]


def test_basic_fetch():
    # Test basic fetch operations
    queue = MRUQueue(3)  # Initial: [1,2,3]
    assert queue.fetch(1) == 1  # After: [2,3,1]
    assert queue.fetch(1) == 2  # After: [3,1,2]
    assert queue.fetch(1) == 3  # After: [1,2,3]
    assert queue.fetch(1) == 1  # After: [2,3,1]


def test_fetch_from_middle():
    # Test fetching from middle positions
    queue = MRUQueue(5)  # Initial: [1,2,3,4,5]
    assert queue.fetch(3) == 3  # After: [1,2,4,5,3]
    assert queue.fetch(3) == 4  # After: [1,2,5,3,4]
    assert queue.fetch(3) == 5  # After: [1,2,3,4,5]


def test_fetch_last_element():
    # Test fetching the last element
    queue = MRUQueue(4)  # Initial: [1,2,3,4]
    assert queue.fetch(4) == 4  # After: [1,2,3,4]
    assert queue.fetch(4) == 4  # After: [1,2,3,4]
    assert queue.fetch(3) == 3  # After: [1,2,4,3]
    assert queue.fetch(4) == 3  # After: [1,2,4,3]


def test_complex_sequence():
    # Test a more complex sequence of operations
    queue = MRUQueue(5)  # Initial: [1,2,3,4,5]
    assert queue.fetch(2) == 2  # After: [1,3,4,5,2]
    assert queue.fetch(2) == 3  # After: [1,4,5,2,3]
    assert queue.fetch(2) == 4  # After: [1,5,2,3,4]
    assert queue.fetch(2) == 5  # After: [1,2,3,4,5]
    assert queue.fetch(1) == 1  # After: [2,3,4,5,1]


def test_sequential_fetch():
    # Test fetching elements sequentially
    queue = MRUQueue(3)  # Initial: [1,2,3]
    assert queue.fetch(1) == 1  # After: [2,3,1]
    assert queue.fetch(1) == 2  # After: [3,1,2]
    assert queue.fetch(1) == 3  # After: [1,2,3]
    assert queue.fetch(1) == 1  # After: [2,3,1]


def test_alternating_positions():
    # Test fetching from alternating positions
    queue = MRUQueue(4)  # Initial: [1,2,3,4]
    assert queue.fetch(1) == 1  # After: [2,3,4,1]
    assert queue.fetch(2) == 3  # After: [2,4,1,3]
    assert queue.fetch(3) == 1  # After: [2,4,3,1]
    assert queue.fetch(4) == 1  # After: [2,4,3,1]


def test_repeated_position():
    # Test fetching repeatedly from the same position
    queue = MRUQueue(5)  # Initial: [1,2,3,4,5]
    assert queue.fetch(2) == 2  # After: [1,3,4,5,2]
    assert queue.fetch(2) == 3  # After: [1,4,5,2,3]
    assert queue.fetch(2) == 4  # After: [1,5,2,3,4]
    assert queue.fetch(2) == 5  # After: [1,2,3,4,5]


def test_large_queue():
    # Test with a larger queue
    queue = MRUQueue(10)  # Initial: [1,2,3,4,5,6,7,8,9,10]
    assert queue.fetch(5) == 5  # After: [1,2,3,4,6,7,8,9,10,5]
    assert queue.fetch(1) == 1  # After: [2,3,4,6,7,8,9,10,5,1]
    assert queue.fetch(10) == 1  # After: [2,3,4,6,7,8,9,10,5,1]
    assert queue.fetch(1) == 2  # After: [3,4,6,7,8,9,10,5,1,2]


def test_edge_cases():
    # Test edge cases
    queue = MRUQueue(1)  # Initial: [1]
    assert queue.fetch(1) == 1  # After: [1]

    queue = MRUQueue(2)  # Initial: [1,2]
    assert queue.fetch(1) == 1  # After: [2,1]
    assert queue.fetch(2) == 1  # After: [2,1]
    assert queue.fetch(1) == 2  # After: [1,2]
