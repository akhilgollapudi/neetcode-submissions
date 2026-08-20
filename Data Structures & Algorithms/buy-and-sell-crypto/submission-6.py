class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_buy = prices[0]
        for current_price in prices:
            sell = current_price - min_buy
            profit = max(sell, profit)
            # if current_price < min_buy:
            #     min_buy = current_price
            min_buy = min(min_buy,current_price)
        return profit