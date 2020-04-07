class Solution:
    def expressiveWords(self, S: str, words) -> int:
        expressive_words = 0
        for word in words:
            i, j = 0, 0
            number_of_consequtive_in_word = 1
            for j in range(0, len(word)):

                if j + 1 < len(word) and word[j + 1] == word[j]:
                    number_of_consequtive_in_word += 1
                    continue

                k = i
                while i < len(S) and S[i] == word[j]:
                    i += 1

                number_of_consequtive_in_S = i - k
                if number_of_consequtive_in_S < 3 and number_of_consequtive_in_S != number_of_consequtive_in_word:
                    i = 0
                    break
                number_of_consequtive_in_word = 1

            if i == len(S) and len(S) >= len(word):
                expressive_words += 1

        return expressive_words