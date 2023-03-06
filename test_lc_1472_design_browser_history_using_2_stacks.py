from lc_1472_design_browser_history_using_2_stacks import BrowserHistory


def test_browser_history():
    history = BrowserHistory("leetcode.com")
    history.visit("dailydictation.com")
    history.visit("facebook.com")
    history.visit("youtube.com")
    got = history.back(1)
    assert got == "facebook.com"
    got = history.back(1)
    assert got == "dailydictation.com"
    got = history.forward(1)
    assert got == "facebook.com"
    history.visit("linkedin.com")
    got = history.forward(2)
    assert got == "linkedin.com"
    got = history.back(2)
    assert got == "dailydictation.com"
    got = history.back(7)
    assert got == "leetcode.com"
