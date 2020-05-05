class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cur = 0
        button_to_ind = {but: i for i, but in enumerate(keyboard)}
        distance = 0
        for ch in word:
            distance += abs(button_to_ind[ch] - cur)
            cur = button_to_ind[ch]

        return distance