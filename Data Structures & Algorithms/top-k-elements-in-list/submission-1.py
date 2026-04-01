class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, values in count.items():
            freq[values].append(key)
        
        ret = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret