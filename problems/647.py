class Solution:
    def countSubstrings(self, s: str) -> int:
        s = [i for i in s]
        count = 0

        def _expand(i, j):
            nonlocal count
            while s[i] == s[j]:
                count += 1

                i -= 1
                j += 1
                if i < 0 or j > len(s) - 1:
                    break

        for i in range(1, len(s) + 1):
            _expand(i - 1, i - 1)
            if i < len(s) and s[i - 1] == s[i]:
                _expand(i - 1, i)

        return count