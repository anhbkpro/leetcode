from bisect import bisect_left
from typing import List


def suggested_products(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    prefix = ''
    res = []
    i = 0
    for c in searchWord:
        prefix += c
        i = bisect_left(products, prefix, i)
        res.append([w for w in products[i:i + 3] if w.startswith(prefix)])
    return res


class Solution:
    pass
