class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(price , minprice)
            profit = price - minprice
            maxprofit = max(profit , maxprofit)
        return maxprofit