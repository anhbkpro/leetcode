from lc_2024_maximize_the_confusion_of_an_exam import maxConsecutiveAnswers


def test_max_consecutive_answers():
    assert maxConsecutiveAnswers("TFFT", 1) == 3
    assert maxConsecutiveAnswers("TTFTTFTT", 1) == 5
