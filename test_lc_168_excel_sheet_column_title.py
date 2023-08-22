from lc_168_excel_sheet_column_title import Solution


def test_convert_to_title():
    assert Solution.convertToTitle(1) == "A"
    assert Solution.convertToTitle(28) == "AB"
    assert Solution.convertToTitle(701) == "ZY"
