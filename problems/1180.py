class Solution:
    def countLetters(self, S: str) -> int:
        picked_char = S[0]
        picked_char_ind = 0
        substrings = 0
        for i in range(len(S)):
            if S[i] != picked_char:
                group_size = i - picked_char_ind
                substrings += (1 + group_size) * group_size // 2
                picked_char = S[i]
                picked_char_ind = i

        last_group_size = len(S) - picked_char_ind
        substrings += (1 + last_group_size) * last_group_size // 2

        return substrings