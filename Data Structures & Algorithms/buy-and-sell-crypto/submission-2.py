class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        The algorithm tries to find the lowest buying price and the highest selling price

        Brutforce: 
        You can find the max_profit by looping and find the (ith price - max(price from the all the numbers to the right))
        Analysis: O(n) space complexity and O(n^2) time complexity

        Optimal:
        We only care about the min price  and the max profit.
        So as we loop we need to keep up with:
        min_price = the lowest number that we have seen so far
        max_profit = the highest profit (highest sell price - lowest buy price) that we have seen so far

        We then compare this with the current profit (current - the lowest price) and assign the 
        max_price the greater number

        We then return -> max_profit.

        """
        
        
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
                
        return max_profit
