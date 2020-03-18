class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strobogrammatic_digits = set(['1', '6', '8', '9', '0'])
        new_num = []
        for digit in num:
            if digit not in strobogrammatic_digits:
                return False
            else:
                if digit == '6':
                    new_num.append('9')
                elif digit == '9':
                    new_num.append('6')
                else:
                    new_num.append(digit)

        return num == ''.join(reversed(new_num))