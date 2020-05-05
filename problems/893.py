from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        groups = Counter()
        for word in A:
            odd_ch = [0] * 26
            even_ch = [0] * 26
            for i in range(len(word)):
                if i & 1 == 0:
                    even_ch[ord(word[i]) - ord('a')] += 1
                else:
                    odd_ch[ord(word[i]) - ord('a')] += 1

            groups[(tuple(odd_ch), tuple(even_ch))] += 1

        return len(groups)