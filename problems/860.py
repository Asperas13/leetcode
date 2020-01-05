class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        l = []

        for bill in bills:
            k = bill - 5

            if k == 5:
                if l.count(5) >= 1:
                    l.remove(5)
                else:
                    return False

            if k == 10:
                if l.count(5) >= 2:
                    for i in range(2):
                        l.remove(5)
                elif l.count(10) >= 1:
                    l.remove(10)
                else:
                    return False

            if k == 15:
                if l.count(5) >= 1 and l.count(10) >= 1:
                    l.remove(5)
                    l.remove(10)
                elif l.count(5) >= 3:
                    for i in range(3):
                        l.remove(5)
                else:
                    return False

            l.append(bill)

        return True