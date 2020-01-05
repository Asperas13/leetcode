class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num)) <= 1:
            return num

        while len(str(num)) > 1:
            res = 0
            for digit in str(num):
                res += int(digit)

            num = res

        return res
