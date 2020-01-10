class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def _permute(cur):
            if len(cur) == len(nums):
                result.append(cur)

            else:
                for i in nums:
                    c = cur.copy()
                    if i not in c:
                        c.append(i)
                        _permute(c)

        _permute([])
        return result