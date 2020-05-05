class Solution:
    def maximum69Number(self, num: int) -> int:
        str_num = str(num)
        changed = False

        new_num = ''
        for digit in str_num:
            if digit == '6' and not changed:
                new_num += '9'
                changed = True
            else:
                new_num += digit

        return new_num