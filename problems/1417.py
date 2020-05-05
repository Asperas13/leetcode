class Solution:
    def reformat(self, s: str) -> str:
        digits_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        letters = [i for i in s if i not in digits_set]
        digits = [i for i in s if i in digits_set]

        if abs(len(letters) - len(digits)) > 1:
            return ''

        i, j = 0, 0

        answer = []

        while i < len(letters) or j < len(digits):
            if i == len(letters):
                answer.append(digits[j])
                j += 1
            elif j == len(digits):
                answer.append(letters[i])
                i += 1
            elif i == j:
                if len(letters) > len(digits):
                    answer.append(letters[i])
                    i += 1
                else:
                    answer.append(digits[j])
                    j += 1

            elif i < j:
                answer.append(letters[i])
                i += 1
            else:
                answer.append(digits[j])
                j += 1

        return ''.join(answer)