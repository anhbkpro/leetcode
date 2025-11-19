import pytest
from arraystrings.total_characters_in_string_after_transformations_i import Solution


def test_length_after_transformations_empty_string():
    solution = Solution()
    assert solution.lengthAfterTransformations("", 1) == 0
    assert solution.lengthAfterTransformations("", 5) == 0


def test_length_after_transformations_zero_transformations():
    solution = Solution()
    assert solution.lengthAfterTransformations("abc", 0) == 3
    assert solution.lengthAfterTransformations("xyz", 0) == 3


def test_length_after_transformations_single_character():
    solution = Solution()
    assert solution.lengthAfterTransformations("a", 1) == 1
    assert solution.lengthAfterTransformations("z", 1) == 2


def test_length_after_transformations_single_transformation():
    solution = Solution()
    # For "abc", after 1 transformation:
    # a->b, b->c, c->a
    assert solution.lengthAfterTransformations("abc", 1) == 3
    # For "xyz", after 1 transformation:
    # x->y, y->z, z->x
    assert solution.lengthAfterTransformations("xyz", 1) == 4


def test_length_after_transformations_multiple_transformations():
    solution = Solution()
    # For "abc", after 2 transformations:
    # First: a->b, b->c, c->a
    # Second: b->c, c->a, a->b
    assert solution.lengthAfterTransformations("abc", 2) == 3
    assert solution.lengthAfterTransformations("xyz", 2) == 5


def test_length_after_transformations_repeated_characters():
    solution = Solution()
    # Test with repeated characters
    assert solution.lengthAfterTransformations("aaa", 1) == 3
    assert solution.lengthAfterTransformations("zzz", 1) == 6


def test_length_after_transformations_modulo_handling():
    solution = Solution()
    # Test that the modulo operation is working correctly
    # Using a large number of transformations
    assert solution.lengthAfterTransformations("abc", 1000) == 725718545
    assert solution.lengthAfterTransformations("xyz", 1000) == 375081919
