"""
My solution if bottom-up. And it works slow because of _could_be_modified method witch takes a lof time to find predecessor
Better approach is to solve in top-down, because for each word with len k it is easy to generate possible successor with len k - 1
Than generate possible predecessor with len k for each word with len k - 1
"""


from collections import defaultdict, Counter


class Solution:
    def longestStrChain(self, words) -> int:
        maximum_chain = 0
        combined_by_length = defaultdict(set)

        def _could_be_modified(word, next_word):
            s1, s2 = Counter(word), Counter(next_word)

            for char in s1:
                if char not in s2:
                    return False

                s2[char] -= 1
                if s2[char] == 0:
                    del s2[char]

            return True

        def _move_through_chain(combined_by_length, word, current_chain_length):
            nonlocal maximum_chain

            combined_by_length[len(word)].discard(word)
            to_visit = [w for w in combined_by_length.get(len(word) + 1, []) if _could_be_modified(word, w)]
            maximum_chain_length = current_chain_length
            for next_word in to_visit:
                maximum_chain_length = max(maximum_chain_length, _move_through_chain(combined_by_length, next_word, current_chain_length + 1))
            return maximum_chain_length

        for w in words:
            combined_by_length[len(w)].add(w)

        for word_len in range(0, 17):
            while combined_by_length[word_len]:
                word = combined_by_length[word_len].pop()
                maximum_chain = max(maximum_chain, _move_through_chain(combined_by_length, word, 1))

        return maximum_chain
