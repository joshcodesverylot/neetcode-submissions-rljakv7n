from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = [[] for i in range(len(nums) + 1)]
        h = {}

        for n in nums:
            h[n] = 1 + h.get(n, 0)
        
        for n, c in h.items():
            b[c].append(n)

        res = []
        for i in range(len(b) - 1, 0, -1):
            for n in b[i]:
                res.append(n)
                if len(res) == k:
                    return res
