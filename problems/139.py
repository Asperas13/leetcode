class Solution:
    def wordBreak(self, s, wordDict):
        memo = {}
        starts = {}
        k = ''
        for letter in s:
            k += letter
            starts[k] = 1

        def _construct(word, memo):
            if len(word) >= len(s):
                return

            if word in memo:
                return True

            for w in wordDict:
                new_word = word + w
                if new_word in starts:
                    _construct(new_word, memo)
                    memo[new_word] = True

        _construct('', memo)
        return memo[s] if s in memo else False