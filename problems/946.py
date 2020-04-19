# pushed: 1 2 3 4 5
#                 i
# popped: 4 3 5 1 2
#               j
# stack [1 2]


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0  # track popped stack

        for i in range(len(pushed)):
            stack.append(pushed[i])
            if stack[-1] == popped[j]:
                while len(stack) and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1

        return len(stack) == 0 and j == len(popped)