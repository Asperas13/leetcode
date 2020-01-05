class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'}': "{", ")": "(", "]": "["}
        for i in s:
            if i in '{[(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    elem = stack.pop()
                    if mapping[i] != elem:
                        return False

        return len(stack) == 0