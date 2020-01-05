class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = ''

        while num > 0:
            binary = str(num % 2) + binary
            num = num // 2

        binary = binary.replace('0', 'a').replace('1', 'b').replace('a', '1').replace('b', '0')

        res = 0

        for i in range(len(binary) - 1, -1, -1):
            if binary[i] == '0':
                pass
            else:
                res += 2 ** (len(binary) - 1 - i)

        return res

