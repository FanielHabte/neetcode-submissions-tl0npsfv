class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # find the max number and minmum number
        # fine the max price and change if you find a bigger number
        # find the lowest price and change as you go
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
                
        return max_profit
