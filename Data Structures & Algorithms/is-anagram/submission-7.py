from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h = {}

        for c in s:
            h[c] = h.get(c, 0) + 1
        
        for c in t:
            h[c] = h.get(c, 0) - 1
        
        for c in h.values():
            if c != 0:
                return False

        return True