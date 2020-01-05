from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        if not paragraph.strip():
            return ''
        words_frequency = Counter()
        banned = {i: 1 for i in banned}
        to_skip = {'!': 1, "?": 1, ",": 1, ";": 1, ".": 1, " ": 1, "": 1, '\'': 1}
        start = 0
        i = 0
        while True:
            if i == len(paragraph):
                word = paragraph[start:i].lower()
                if word and word not in banned:
                    words_frequency[word] += 1
                break

            char = paragraph[i]

            if char in to_skip:
                word = paragraph[start:i].lower()
                if word and word not in banned:
                    words_frequency[word] += 1
                start = i + 1
            i += 1
        return words_frequency.most_common(1)[0][0]