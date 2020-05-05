from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_c = Counter(ransomNote)
        m_c = Counter(magazine)

        return all(rn_c[i] <= m_c[i] for i in rn_c)