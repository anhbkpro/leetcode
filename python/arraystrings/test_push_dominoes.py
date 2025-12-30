import pytest

from .push_dominoes import Solution


@pytest.mark.parametrize(
    "input_dominoes, expected_output",
    [
        (".L.R...LR..L..", "LL.RR.LLRRLL.."),
        ("RR.L", "RR.L"),
        (".", "."),
        ("L", "L"),
        ("R", "R"),
        ("", ""),
        ("R.L", "R.L"),
        ("...L...R...", "LLLL...RRRR"),
        ("R...L", "RR.LL"),
        ("R.R.L", "RRR.L"),
        ("L.....R", "L.....R"),
        ("R.....L", "RRR.LLL"),
    ],
)
def test_push_dominoes(input_dominoes: str, expected_output: str):
    solution = Solution()
    actual_output = solution.push_dominoes(input_dominoes)
    assert actual_output == expected_output
