class Solution:
    def dailyTemperatures(self, T):
        if len(T) < 2:
            return [] if len(T) == 0 else [0]

        stack = [0]
        result = [0] * len(T)

        for i in range(1, len(T)):
            if T[i] <= T[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                while stack and T[i] > T[stack[len(stack) - 1]]:
                    j = stack.pop()
                    result[j] = i - j

                stack.append(i)

        return result
