from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = [info for info in details if int(info[-4:-2]) > 60]
        return len(seniors)
