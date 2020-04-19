def collect_text(string):
    stack_S = []
    for i in range(len(string)):
        if string[i] == '#':
            if stack_S:
                stack_S.pop()
        else:
            stack_S.append(string[i])

    return stack_S


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return collect_text(S) == collect_text(T)