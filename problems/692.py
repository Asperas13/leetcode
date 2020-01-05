from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        words_frequency = Counter()
        words.sort()
        for word in words:
            words_frequency[word] += 1

        return [i[0] for i in words_frequency.most_common(k)]