class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = [[] for i in range(len(nums) + 1)]
        h = {}

        for n in nums:
            h[n] = h.get(n, 0) + 1
        
        for n, c in h.items():
            b[c].append(n)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in b[i]:
                res.append(n)
                if len(res) == k:
                    return res