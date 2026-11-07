class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")  # cheapest price seen so far
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # better day to buy
            else:
                max_profit = max(max_profit, price - min_price)  # selling today

        return max_profit