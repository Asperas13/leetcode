class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local, domain = email.split('@')
            if not local or not domain:
                continue
            handled_email = []
            for char in local:
                if char == '.':
                    continue
                elif char == '+':
                    break
                else:
                    handled_email.append(char)
            handled_email.append('@')
            handled_email.append(domain)
            email_set.add(''.join(handled_email))

        return len(email_set)
