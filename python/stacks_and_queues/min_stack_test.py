import unittest
from .min_stack import MinStack


class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.stack = MinStack()

    def test_example_1(self):
        self.stack.push(-2)
        self.stack.push(0)
        self.stack.push(-3)

        self.assertEqual(self.stack.getMin(), -3)
        self.stack.pop()
        self.assertEqual(self.stack.top(), 0)
        self.assertEqual(self.stack.getMin(), -2)

    def test_empty_stack_operations(self):
        # Test that operations on empty stack return None
        self.stack.pop()  # Should not raise exception
        self.assertIsNone(self.stack.top())  # Should return None for empty stack
        self.assertIsNone(self.stack.getMin())  # Should return None for empty stack

    def test_single_element(self):
        self.stack.push(5)
        self.assertEqual(self.stack.top(), 5)
        self.assertEqual(self.stack.getMin(), 5)
        self.stack.pop()
        self.assertIsNone(self.stack.top())
        self.assertIsNone(self.stack.getMin())

    def test_duplicate_elements(self):
        self.stack.push(1)
        self.stack.push(1)
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)
        self.assertEqual(self.stack.top(), 1)

    def test_ascending_order(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.getMin(), 1)
        self.assertEqual(self.stack.top(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)
        self.assertEqual(self.stack.top(), 2)

    def test_descending_order(self):
        self.stack.push(3)
        self.stack.push(2)
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)
        self.assertEqual(self.stack.top(), 1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 2)
        self.assertEqual(self.stack.top(), 2)

    def test_mixed_operations(self):
        self.stack.push(-2)
        self.assertEqual(self.stack.getMin(), -2)
        self.stack.push(0)
        self.assertEqual(self.stack.getMin(), -2)
        self.stack.push(-1)
        self.assertEqual(self.stack.getMin(), -2)
        self.assertEqual(self.stack.top(), -1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), -2)

    def test_alternating_min(self):
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.push(0)
        self.assertEqual(self.stack.getMin(), 0)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)


if __name__ == "__main__":
    unittest.main()
