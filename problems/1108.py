class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_ip = []

        for token in address:
            if token == '.':
                defanged_ip.append('[')
                defanged_ip.append('.')
                defanged_ip.append(']')
            else:
                defanged_ip.append(token)

        return ''.join(defanged_ip)