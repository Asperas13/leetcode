from string import ascii_lowercase


class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        values = dict(zip(ascii_lowercase, widths))
        last = 0
        page_count = 0

        for i in S:
            last += values[i]

            if last > 100:
                page_count += 1
                last = values[i]
        if last != 0:
            page_count += 1

        return [page_count, last]