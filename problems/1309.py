class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ch_code = int(s[i - 2] + s[i - 1])
                i -= 3
            else:
                ch_code = int(s[i])
                i -= 1
            decrypted.append(chr(ord('a') + ch_code - 1))

        return ''.join(list(reversed(decrypted)))