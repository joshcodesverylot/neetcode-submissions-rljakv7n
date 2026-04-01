class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while nums:
            j = len(nums) - 1
            popped = nums.pop()
            sub = target - popped
            if sub in nums:
                return [nums.index(sub), j]