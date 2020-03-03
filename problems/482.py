class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        unformatted = ''.join([char.upper() for char in S if char != '-'])
        i, j = 0, len(unformatted)
        groups = []
        while True:
            if j == 0:
                if i != 0:
                    groups.append(''.join(unformatted[j:j + i]))
                break
            elif i == K:
                groups.append(''.join(unformatted[j:j + i]))
                i = 0
            else:
                i += 1
                j -= 1

        return '-'.join(reversed(groups))
