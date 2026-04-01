class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         h = {}
         for i in nums:
            h[i] = h.get(i, 0) + 1
            val = h[i]
            if val > 1:
                return True
         return False