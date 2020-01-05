class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_to_ind = {}
        for i, num in enumerate(nums):
            j = int_to_ind.get(target - num, None)
            if j is not None:
                return (j, i)
            int_to_ind[num] = i

        return (-1, -1)