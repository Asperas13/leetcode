class Solution:
    def coinChange(self, coins, amount: int) -> int:

        coins = sorted(coins)
        dp = [float('+inf') for _ in range(amount + 1)]
        dp[0] = 0

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i - c] + 1, dp[i])

        return dp[amount] if dp[amount] != float('+inf') else -1