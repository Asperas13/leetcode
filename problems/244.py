from collections import defaultdict


class WordDistance:

    def __init__(self, words: List[str]):
        self.distances = defaultdict(set)
        for i, w1 in enumerate(words):
            self.distances[w1].add(i)

    def shortest(self, word1: str, word2: str) -> int:
        m = float('+inf')
        for i in self.distances[word1]:
            for j in self.distances[word2]:
                if abs(j - i) < m:
                    m = abs(j - i)

        return m

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)