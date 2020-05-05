class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        i, j = 0, 0

        modified = ''
        op = 0
        while i < len(S) and j < len(S):
            if S[j] == '(':
                op += 1
            else:
                op -= 1

            if op == 0:
                for k in range(i + 1, j):
                    modified += S[k]
                i = j + 1
            j += 1

        return modified