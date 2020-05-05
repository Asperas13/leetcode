class Solution:
    def sortString(self, s: str) -> str:
        counter = [0] * 26

        for ch in s:
            counter[ord(ch) - ord('a')] += 1

        new_string = ''
        while True:
            letters_remain = False

            for i in range(len(counter)):
                if counter[i] > 0:
                    letters_remain = True
                    new_string += chr(ord('a') + i)
                    counter[i] -= 1

            if not letters_remain:
                break

            letters_remain = False
            for i in range(len(counter) - 1, -1, -1):
                if counter[i] > 0:
                    letters_remain = True
                    new_string += chr(ord('a') + i)
                    counter[i] -= 1

            if not letters_remain:
                break

        return new_string