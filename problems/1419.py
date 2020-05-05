from collections import Counter


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if not croakOfFrogs:
            return 0

        cur_to_prev = {'r': 'c', 'k': 'a', 'a': 'o', 'o': 'r', 'c': 'c'}

        d = Counter({'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0})
        min_frogs = 1
        for ch in croakOfFrogs:
            d[ch] += 1
            min_ch, max_ch = d['c'], d['c']
            for l in d:
                if d[l] < min_ch:
                    min_ch = d[l]
                if d[l] > max_ch:
                    max_ch = d[l]
                if d[l] > d[cur_to_prev[l]]:
                    return -1

            min_frogs = max(min_frogs, max_ch)
            if min_ch != 0:
                for l in d:
                    d[l] -= 1
        for l in d:
            if d[l] > 0:
                return -1

        return min_frogs