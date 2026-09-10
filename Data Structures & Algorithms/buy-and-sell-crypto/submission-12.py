class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = i + 1
        Maxp = 0
        while j <= len(prices) - 1:
            profit = 0
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                Maxp = max(Maxp, profit)
                j += 1
            else:
                i = j
                j += 1
        return Maxp