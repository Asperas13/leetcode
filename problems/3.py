class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        longest = 0
        ptr1, ptr2 = 0, 0
        while ptr2 != len(s):
            if s[ptr2] not in window:
                window[s[ptr2]] = 1
                longest = max(longest, len(window))
                ptr2 += 1
            else:
                window[s[ptr2]] += 1
                while window[s[ptr2]] == 2:
                    window[s[ptr1]] -= 1
                    if window[s[ptr1]] == 0:
                        window.pop(s[ptr1])
                    ptr1 += 1
                ptr2 += 1
        longest = max(longest, len(window))
        return longest
