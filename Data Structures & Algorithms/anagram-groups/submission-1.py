from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)


        for s in strs:
            h[tuple(sorted(s))].append(s)

        return list(h.values())