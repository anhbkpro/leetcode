from lc_1055_shortest_way_to_form_string_two_pointers import shortestWay


def test_shortest_way():
    assert shortestWay(source="abc", target="abcbc") == 2
    assert shortestWay(source="abc", target="acdbc") == -1
