from string import ascii_lowercase, ascii_uppercase


class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        letters = dict(list(zip(ascii_uppercase, ascii_lowercase)))

        for i in range(len(str)):
            if letters.get(str[i], ''):
                str = str[:i] + letters[str[i]] + str[i + 1:]

        return str
