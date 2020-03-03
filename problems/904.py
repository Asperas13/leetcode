from collections import Counter


class Solution:
    def totalFruit(self, tree) -> int:
        max_fruits = 0
        fruits = Counter()
        i, j = 0, 0
        while j <= len(tree):
            if (j == len(tree) and len(fruits) > 2) or len(fruits) > 2:
                while len(fruits) != 2:
                    fruits[tree[i]] -= 1
                    if fruits[tree[i]] == 0:
                        del fruits[tree[i]]
                    i += 1
            elif j == len(tree):
                max_fruits = max(max_fruits, j - i)
                break
            else:
                fruits[tree[j]] += 1
                j += 1

            if len(fruits) == 2:
                max_fruits = max(max_fruits, j - i)

        return max_fruits
