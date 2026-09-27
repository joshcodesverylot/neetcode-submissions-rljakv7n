class Solution:
    def isValid(self, s: str) -> bool:
        h = {
            "}": "{",
            "]": "[",
            ")": "("
            }
        stack = []
        for i in s:
            if i not in h:
                stack.append(i)
            else:
                if stack and stack[-1] == h[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
                    