class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_to_word = {}
        words = str.split(' ')
        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)):
            return False
        size = len(words)
        for i in range(size):
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = words[i]
            else:
                if pattern_to_word[pattern[i]] != words[i]:
                    return False

        return True
    