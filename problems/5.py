class Solution:
    def longestPalindrome(self, s: str) -> str:
        corner_min, corner_max = 0, len(s) - 1
        max_palindrom = ""

        def _expand(left, right, s):
            nonlocal corner_min, corner_max, max_palindrom
            while True:
                left -= 1
                right += 1
                if left < corner_min or right > corner_max or s[left] != s[right]:
                    break

            if len(max_palindrom) < right - (left + 1):
                max_palindrom = s[left + 1:right]

        for i, char in enumerate(s):
            _expand(i, i, s)
            if i + 1 <= corner_max and s[i] == s[i + 1]:
                _expand(i, i + 1, s)

        return max_palindrom