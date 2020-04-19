class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrom(i, j):
            while i < j:
                if s[i] != s[j]:
                    return (False, i, j)
                i += 1
                j -= 1

            return True, i, j

        is_palindrom_wout_removes, i, j = is_palindrom(0, len(s) - 1)
        if not is_palindrom_wout_removes:
            return is_palindrom(i + 1, j)[0] or is_palindrom(i, j - 1)[0]

        return True