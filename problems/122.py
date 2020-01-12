class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - buy > 0:
                profit += prices[i] - buy
            buy = prices[i]

        return profit