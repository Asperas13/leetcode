class Solution(object):
    def numDecodings(self, s):
        memo = {}

        def recurse(k):

            if k < 0:
                return 1

            if k in memo:
                return memo[k]

            memo[k] = 0
            if s[k - 1:k + 1] and 10 <= int(s[k - 1:k + 1]) <= 26:
                memo[k] += recurse(k - 2)
            if s[k] != '0':
                memo[k] += recurse(k - 1)
            return memo[k]

        recurse(len(s) - 1)
        return memo.get(len(s) - 1, 0)