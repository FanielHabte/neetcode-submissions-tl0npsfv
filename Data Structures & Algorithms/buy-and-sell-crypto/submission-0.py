class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # find the max number and minmum number
        # fine the max price and change if you find a bigger number
        # find the lowest price and change as you go
        max_profit = 0
        for i in range(len(prices)):
            profit =  max(prices[i:]) - prices[i]
            if profit > max_profit:
                max_profit = profit
                
        return max_profit
