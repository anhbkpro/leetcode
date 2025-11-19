from .kth_largest_element_in_a_stream_maintain_sorted_list import KthLargest


def test_kth_largest_element_in_a_stream():
    kth_largest = KthLargest(3, [4, 5, 8, 2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8
