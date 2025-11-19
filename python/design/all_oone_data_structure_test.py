from .all_oone_data_structure import AllOne


def test_all_oone_data_structure():
    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("hello")
    allOne.getMaxKey()  # return "hello"
    allOne.getMinKey()  # return "hello"
    allOne.inc("leet")
    allOne.getMaxKey()  # return "hello"
    allOne.getMinKey()  # return "leet"
