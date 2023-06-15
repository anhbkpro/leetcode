from lc_1268_search_suggestions_system import suggested_products


def test_suggested_products():
    assert suggested_products(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse") == [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
