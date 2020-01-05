from string import ascii_lowercase

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        morse = [".-","-...","-.-.","-..",
                 ".","..-.","--.","....",
                 "..",".---","-.-",".-..",
                 "--","-.","---",".--.",
                 "--.-",".-.","...","-",
                 "..-","...-",".--",
                 "-..-","-.--","--.."]

        return len(set([''.join([morse[ascii_lowercase.find(i)] for i in word]) for word in words]))