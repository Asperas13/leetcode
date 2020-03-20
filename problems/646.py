"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [0 for _ in range(len(pairs))]
        pairs.sort(key=lambda pair: pair[0])
        for i in range(len(pairs) - 1, -1, -1):
            greater_chain = 0
            for j in range(i + 1, len(pairs)):
                if pairs[j][0] > pairs[i][1]:
                    greater_chain = max(greater_chain, 1 + dp[j])

            dp[i] = greater_chain

        return max(dp) + 1
"""


class Solution(object):
    def findLongestChain(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key=lambda pair: pair[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans