from .parsing_a_boolean_expression import Solution


def test_parsing_a_boolean_expression():
    assert Solution().parseBoolExpr(expression="!(f)") is True
    assert Solution().parseBoolExpr(expression="|(f,t)") is True
