class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = float('inf')
        running_profit = 0

        for i in prices:
            running_min = min(running_min, i)
            if i - running_min > running_profit:
                running_profit = i - running_min
            
        return running_profit

