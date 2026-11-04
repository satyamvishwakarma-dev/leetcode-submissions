from bisect import bisect_right
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()  # sort by price

        # Make beauty the best-so-far (running max)
        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        prices = [price for price, _ in items]
        result = []

        for money in queries:
            i = bisect_right(prices, money)  # how many items are affordable
            result.append(items[i - 1][1] if i > 0 else 0)

        return result