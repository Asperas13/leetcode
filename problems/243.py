class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortest = float("+inf")
        first = None
        second = None
        for i, word in enumerate(words):
            if word == word1:
                first = i
                if second is not None:
                    shortest = min(shortest, abs(second - first)) if shortest else abs(second - first)

            if word == word2:
                second = i
                if first is not None:
                    shortest = min(shortest, abs(second - first)) if shortest else abs(second - first)

        return shortest