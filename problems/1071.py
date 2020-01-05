class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_string = min(str1, str2, key=len)
        max_string = str1 if min_string != str1 else str2
        min_string_len = len(min_string)
        max_string_len = len(max_string)
        largest_divider = ""
        cur_divider = ""
        cur_divider_len = 0
        for letter in min_string:
            cur_divider += letter
            cur_divider_len += 1
            if min_string_len % cur_divider_len == 0 and max_string_len % cur_divider_len == 0:
                if cur_divider * (min_string_len // cur_divider_len) == min_string and cur_divider * (max_string_len // cur_divider_len) == max_string and cur_divider_len > len(largest_divider):
                    largest_divider = cur_divider
        return largest_divider