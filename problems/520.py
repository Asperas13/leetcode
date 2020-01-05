class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if not word:
            return False

        return word == word.upper() or word == word.lower() or word.capitalize() == word