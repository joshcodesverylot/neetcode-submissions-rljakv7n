class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l + 1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                maxP = prices[r] - prices[l]
                profit = max(maxP, profit)
            else:
                l = r
            r += 1
        return profit