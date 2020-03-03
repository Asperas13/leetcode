from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = Counter(t)
        window2 = Counter()
        required = set(t)
        min_window = ""
        i, j = 0, 0

        while j < len(s):
            if s[j] in window:
                window2[s[j]] += 1
                if window[s[j]] == window2[s[j]] and s[j] in required:
                    required.remove(s[j])

                while not required:
                    if not min_window or j + 1 - i < len(min_window):
                        min_window = s[i:j + 1]

                    if s[i] in window:
                        window2[s[i]] -= 1
                        if window2[s[i]] < window[s[i]]:
                            required.add(s[i])

                    i += 1
            j += 1

        return min_window