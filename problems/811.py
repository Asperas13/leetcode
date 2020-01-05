from collections import Counter


def concat(number, domain):
    return str(number) + ' ' + domain


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        c = Counter()

        for dom in cpdomains:
            count, domains = dom.split(' ')
            domains = domains.split('.')
            for i in range(len(domains)):
                c['.'.join(domains[i:])] += int(count)

        return [concat(c[i], i) for i in c]
