from .product_of_the_last_k_numbers import ProductOfNumbers
import pytest


@pytest.fixture
def product():
    return ProductOfNumbers()


def test_basic_operations(product):
    product.add(3)
    product.add(2)
    product.add(4)
    assert product.getProduct(2) == 8  # 2 * 4
    assert product.getProduct(3) == 24  # 3 * 2 * 4
    product.add(5)
    assert product.getProduct(2) == 20  # 4 * 5
    assert product.getProduct(3) == 40  # 2 * 4 * 5
    assert product.getProduct(4) == 120  # 3 * 2 * 4 * 5


def test_operations_with_zero(product):
    product.add(3)
    product.add(0)
    product.add(2)
    product.add(4)
    assert product.getProduct(2) == 8  # 2 * 4
    assert product.getProduct(3) == 0  # includes 0, so product is 0
    assert product.getProduct(4) == 0  # includes 0, so product is 0
    product.add(5)
    assert product.getProduct(2) == 20  # 4 * 5
    assert product.getProduct(3) == 40  # 2 * 4 * 5


def test_single_number(product):
    product.add(5)
    assert product.getProduct(1) == 5


def test_multiple_zeros(product):
    product.add(2)
    product.add(0)
    product.add(3)
    product.add(0)
    product.add(4)
    assert product.getProduct(1) == 4
    assert product.getProduct(2) == 0
    assert product.getProduct(3) == 0
    assert product.getProduct(4) == 0
    assert product.getProduct(5) == 0


def test_k_equals_stream_size(product):
    product.add(2)
    product.add(3)
    product.add(4)
    assert product.getProduct(3) == 24  # 2 * 3 * 4


def test_large_numbers(product):
    product.add(1000)
    product.add(2000)
    product.add(3000)
    assert product.getProduct(2) == 6000000  # 2000 * 3000
    assert product.getProduct(3) == 6000000000  # 1000 * 2000 * 3000


def test_consecutive_zeros(product):
    product.add(2)
    product.add(0)
    product.add(0)
    product.add(3)
    assert product.getProduct(1) == 3
    assert product.getProduct(2) == 0
    assert product.getProduct(3) == 0
    assert product.getProduct(4) == 0


def test_alternating_zeros(product):
    product.add(2)
    product.add(0)
    product.add(3)
    product.add(0)
    product.add(4)
    product.add(0)
    assert product.getProduct(1) == 0
    assert product.getProduct(2) == 0
    assert product.getProduct(3) == 0
    product.add(5)
    assert product.getProduct(1) == 5
    assert product.getProduct(2) == 0


def test_k_larger_than_stream(product):
    product.add(2)
    product.add(3)
    assert product.getProduct(3) == 0  # k > stream size
    product.add(4)
    assert product.getProduct(4) == 0  # k > stream size
