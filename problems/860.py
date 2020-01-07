class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 5:
                s[5] += 1
            elif i == 10:
                if s[5] > 0:
                    s[5] -= 1
                    s[10] += 1
                else:
                    return False
            else:
                if s[5] > 0 and s[10] > 0:
                    s[5] -= 1
                    s[10] -= 1
                    s[20] += 1
                elif s[5] >= 3:
                    s[5] -= 3
                    s[20] += 1
                else:
                    return False
        return True