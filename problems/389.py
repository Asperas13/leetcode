class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for letter in t:
            if t.count(letter) > s.count(letter):
                return letter
