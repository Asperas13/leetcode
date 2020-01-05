class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'

        return [i for i in words if (all(p in row1 for p in i.lower()) or all(p in row2 for p in i.lower()) or all(
            p in row3 for p in i.lower()))]
