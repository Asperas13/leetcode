from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for string in strs:
            anagram = [l for l in string]
            anagram.sort()
            anagram = ''.join(anagram)
            anagrams[anagram].append(string)

        return anagrams.values()