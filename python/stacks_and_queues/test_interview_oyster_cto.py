import pytest

from .interview_oyster_cto import calculate


@pytest.fixture
def test_cases():
    return {
        "simple_add": {"input": "( add 2 5 )", "expected": 7},
        "simple_mul": {"input": "( mul 2 4 )", "expected": 8},
        "nested_add_mul": {"input": "( add 2 ( mul 2 2 ) )", "expected": 6},
        "nested_mul_add": {"input": "( mul ( mul 2 2 ) ( add 1 3 ) )", "expected": 16},
        "negative_numbers": {"input": "( add -2 -3 )", "expected": -5},
        "mixed_negative_positive": {"input": "( mul -2 3 )", "expected": -6},
        "deeply_nested": {
            "input": "( add ( mul 2 3 ) ( add ( mul 2 2 ) 1 ) )",
            "expected": 11,
        },
        "multiple_operations": {
            "input": "( add ( add 1 2 ) ( add 3 4 ) )",
            "expected": 10,
        },
    }


def test_simple_add(test_cases):
    assert (
        calculate(test_cases["simple_add"]["input"])
        == test_cases["simple_add"]["expected"]
    )


def test_simple_mul(test_cases):
    assert (
        calculate(test_cases["simple_mul"]["input"])
        == test_cases["simple_mul"]["expected"]
    )


def test_nested_add_mul(test_cases):
    assert (
        calculate(test_cases["nested_add_mul"]["input"])
        == test_cases["nested_add_mul"]["expected"]
    )


def test_nested_mul_add(test_cases):
    assert (
        calculate(test_cases["nested_mul_add"]["input"])
        == test_cases["nested_mul_add"]["expected"]
    )


def test_negative_numbers(test_cases):
    assert (
        calculate(test_cases["negative_numbers"]["input"])
        == test_cases["negative_numbers"]["expected"]
    )


def test_mixed_negative_positive(test_cases):
    assert (
        calculate(test_cases["mixed_negative_positive"]["input"])
        == test_cases["mixed_negative_positive"]["expected"]
    )


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate("( div 2 3 )")


def test_malformed_expression():
    with pytest.raises(Exception):
        calculate("add 2 3")


def test_empty_expression():
    with pytest.raises(Exception):
        calculate("")


def test_single_number():
    with pytest.raises(Exception):
        calculate("( 5 )")


def test_missing_operator():
    with pytest.raises(Exception):
        calculate("( 2 3 )")


def test_missing_operand():
    with pytest.raises(Exception):
        calculate("( add 2 )")
