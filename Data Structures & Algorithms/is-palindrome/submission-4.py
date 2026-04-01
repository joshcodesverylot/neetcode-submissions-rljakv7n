class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l1 = [char.lower() for char in s if char not in ["!", ",", ".", ":", "'", "?", " "]]
        i = 0
        j = len(l1) - 1
        
        while i < j:
            if l1[i] != l1[j]:
                return False
            i += 1
            j -= 1
        return True
