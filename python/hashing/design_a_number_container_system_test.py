import unittest

from .design_a_number_container_system import NumberContainers


class TestNumberContainers(unittest.TestCase):
    def setUp(self):
        self.obj = NumberContainers()

    def test_example_1(self):
        self.obj.change(1, 1)
        self.obj.change(2, 2)
        self.assertEqual(self.obj.find(1), 1)
        self.assertEqual(self.obj.find(2), 2)
        self.obj.change(1, 2)
        self.assertEqual(self.obj.find(1), -1)
        self.assertEqual(self.obj.find(2), 1)

    def test_example_2(self):
        self.assertEqual(self.obj.find(10), -1)
        self.obj.change(2, 10)
        self.obj.change(1, 10)
        self.obj.change(3, 10)
        self.obj.change(5, 10)
        self.assertEqual(self.obj.find(10), 1)
        self.obj.change(1, 20)
        self.assertEqual(self.obj.find(10), 2)


if __name__ == "__main__":
    unittest.main()
