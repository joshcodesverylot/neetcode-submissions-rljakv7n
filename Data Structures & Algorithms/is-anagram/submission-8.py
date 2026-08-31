class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        
        for x in s:
            if x not in h1:
                h1[x] = 1
            else:
                h1[x] += 1

        for y in t:
            if y not in h2:
                h2[y] = 1
            else:
                h2[y] += 1
        
        if h1 == h2:
            return True
        return False