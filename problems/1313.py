class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i], nums[i + 1]
            decompressed_val = [val] * freq
            decompressed.extend(decompressed_val)

        return decompressed