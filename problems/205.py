class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        for i, j in zip(s, t):
            if i not in mapping1:
                mapping1[i] = j
            else:
                if mapping1[i] != j:
                    return False

            if j not in mapping2:
                mapping2[j] = i
            else:
                if mapping2[j] != i:
                    return False
        return True