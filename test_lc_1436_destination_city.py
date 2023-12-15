from lc_1436_destination_city import Solution


def test_dest_city():
    assert Solution.dest_city(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]) == "Sao Paulo"
    assert Solution.dest_city(paths=[["B", "C"], ["D", "B"], ["C", "A"]]) == "A"
