class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in h:
                return [h[complement], i]
            h[n] = i