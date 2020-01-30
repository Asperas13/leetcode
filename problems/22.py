class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        if not n:
            return parentheses

        def _generate(cur, left, right, n):
            if len(cur) == 2 * n:
                parentheses.append(''.join(cur))
            elif left == n:
                while len(cur) < 2 * n:
                    cur.append(')')
                parentheses.append(''.join(cur))
            else:
                if right < left:
                    cur_copy = cur.copy()
                    cur_copy.append(')')
                    _generate(cur_copy, left, right + 1, n)
                cur.append('(')
                _generate(cur, left + 1, right, n)

        _generate([], 0, 0, n)
        return parentheses
