class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [i for i in range(left, right + 1) if '0' not in str(i) and all(int(i) % int(j) == 0 for j in str(i))]
