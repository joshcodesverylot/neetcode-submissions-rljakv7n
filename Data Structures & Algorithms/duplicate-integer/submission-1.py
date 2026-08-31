class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = dict()
        for n in nums:
            n = str(n)
            if n not in h:
                h[n] = 1
            else:
                return True
        return False