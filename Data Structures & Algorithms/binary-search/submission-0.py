class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            avg = (r + l) // 2
            if target > nums[avg]:
                l = avg + 1
            elif target < nums[avg]:
                r = avg - 1
            else:
                return avg
        return -1