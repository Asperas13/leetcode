from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = Counter()
        longest_substring = 0
        i = 0

        def decrease(window, char):
            window[char] -= 1
            if window[char] == 0:
                window.pop(char)

        for j in range(len(s)):
            window[s[j]] += 1
            while len(window) == 3:
                longest_substring = max(longest_substring, j - i)
                decrease(window, s[i])
                i += 1

            longest_substring = max(longest_substring, j - i)

        if i != len(s):
            if len(window) < 3:
                longest_substring = max(longest_substring, len(s) - i)
            decrease(window, s[i])
            i += 1

        return longest_substring