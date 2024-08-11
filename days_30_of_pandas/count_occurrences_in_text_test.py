from .count_occurrences_in_text import count_occurrences
import pandas as pd


def test_count_occurrences():
    # Input:
    # Files table:
    # +------------+----------------------------------------------------------------------------------+
    # | file_name  | content                                                                         |
    # +------------+----------------------------------------------------------------------------------+
    # | draft1.txt | The stock exchange predicts a bull market which would make many investors happy. |
    # | draft2.txt | The stock exchange predicts a bull market which would make many investors happy, |
    # |            | but analysts warn of possibility of too much optimism and that in fact we are    |
    # |            | awaiting a bear market.                                                          |
    # | draft3.txt | The stock exchange predicts a bull market which would make many investors happy, |
    # |            | but analysts warn of possibility of too much optimism and that in fact we are    |
    # |            | awaiting a bear market. As always predicting the future market is an uncertain   |
    # |            | game and all investors should follow their instincts and best practices.         |
    # +------------+----------------------------------------------------------------------------------+
    # Output:
    # +------+-------+
    # | word | count |
    # +------+-------+
    # | bull | 3     |
    # | bear | 2     |
    # +------+-------+
    files = {
        "file_name": ["draft1.txt", "draft2.txt", "draft3.txt"],
        "content": [
            "The stock exchange predicts a bull market which would make many investors happy.",
            "The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market.",
            "The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices.",
        ],
    }
    files = pd.DataFrame(files)
    expected = {"word": ["bull", "bear"], "count": [3, 2]}
    expected = pd.DataFrame(expected)
    assert count_occurrences(files)["word"].to_list() == expected["word"].to_list()
    assert count_occurrences(files)["count"].to_list() == expected["count"].to_list()
