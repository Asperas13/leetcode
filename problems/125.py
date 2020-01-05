from string import ascii_lowercase, digits


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        alphabet = {i: 1 for i in ascii_lowercase + digits}
        i, j = 0, len(s) - 1

        while i < j:
            while s[i].lower() not in alphabet:
                i += 1
                if i > j:
                    return True
            while s[j].lower() not in alphabet:
                j -= 1
                if i > j:
                    return True

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
        return True