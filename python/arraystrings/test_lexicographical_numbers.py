import unittest
from .lexicographical_numbers import Solution


class TestLexicographicalNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_single_digit(self):
        n = 5
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_power_of_ten(self):
        n = 10
        expected = [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_minimum_input(self):
        n = 1
        expected = [1]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_two_digit_numbers(self):
        n = 20
        expected = [
            1,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            2,
            20,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_three_digit_numbers(self):
        n = 100
        expected = [
            1,
            10,
            100,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            2,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            3,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            4,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            48,
            49,
            5,
            50,
            51,
            52,
            53,
            54,
            55,
            56,
            57,
            58,
            59,
            6,
            60,
            61,
            62,
            63,
            64,
            65,
            66,
            67,
            68,
            69,
            7,
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            8,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            89,
            9,
            90,
            91,
            92,
            93,
            94,
            95,
            96,
            97,
            98,
            99,
        ]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_leetcode_example(self):
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_numbers_with_nines(self):
        n = 19
        expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_numbers_with_zeros(self):
        n = 20
        expected = [
            1,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            2,
            20,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
        ]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_large_number(self):
        n = 50
        expected = [
            1,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            2,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            27,
            28,
            29,
            3,
            30,
            31,
            32,
            33,
            34,
            35,
            36,
            37,
            38,
            39,
            4,
            40,
            41,
            42,
            43,
            44,
            45,
            46,
            47,
            48,
            49,
            5,
            50,
            6,
            7,
            8,
            9,
        ]
        self.assertEqual(self.solution.lexicalOrder(n), expected)

    def test_very_large_input(self):
        n = 1000
        result = self.solution.lexicalOrder(n)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], 1)
        # Verify the order is lexicographical
        for i in range(len(result) - 1):
            self.assertLess(str(result[i]), str(result[i + 1]))


if __name__ == "__main__":
    unittest.main()
