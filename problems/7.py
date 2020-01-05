class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if '-' in x:
            if int(x[:0:-1]) < 2147483648:
                return int('-' + x[:0:-1])
            else:
                return 0
        else:
            if int(x[::-1]) < 2147483648:
                return int(x[::-1])
            else:
                return 0
