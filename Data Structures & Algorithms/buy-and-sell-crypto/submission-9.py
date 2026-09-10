class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        max_profit = 0
        while j <= len(prices) - 1:
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                j += 1
            else:
                i = j
                j += 1
        return max_profit