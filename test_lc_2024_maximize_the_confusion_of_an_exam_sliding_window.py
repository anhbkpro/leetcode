from lc_2024_maximize_the_confusion_of_an_exam_sliding_window import maxConsecutiveAnswersSlidingWindow


def test_max_consecutive_answers():
    assert maxConsecutiveAnswersSlidingWindow("TFFT", 1) == 3
    assert maxConsecutiveAnswersSlidingWindow("TTFTTFTT", 1) == 5
