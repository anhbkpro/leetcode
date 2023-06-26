from lc_616_add_bold_tag_in_string import addBoldTag


def test_add_bold_tag():
    assert addBoldTag("abcxyz123", ["abc", "123"]) == "<b>abc</b>xyz<b>123</b>"
    assert addBoldTag("aaabbcc", ["aaa", "aab", "bc"]) == "<b>aaabbc</b>c"
