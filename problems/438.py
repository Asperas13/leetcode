from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        result = []
        window1, window2 = Counter(p), Counter(s[:len(p) - 1])
        for i in range(len(s) - len(p) + 1):
            f, l = s[i], s[i + len(p) - 1]
            window2[l] += 1
            if window1 == window2:
                result.append(i)
            if window2[f] > 1:
                window2[f] -= 1
            else:
                window2.pop(f)

        return result
