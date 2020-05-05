class Solution:
    def removeVowels(self, S: str) -> str:
        wo_vowels = []
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for ch in S:
            if ch not in vowels:
                wo_vowels.append(ch)

        return ''.join(wo_vowels)