class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        stack = []
        for t in tokens:
            if t == "+":
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                total = t2 + t1
                stack.append(total)
            elif t == "-":
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                total = t2 - t1
                stack.append(total)
            elif t == "*":
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                total = t2 * t1
                stack.append(total)
            elif t == "/":
                t1 = int(stack.pop())
                t2 = int(stack.pop())
                total = t2 / t1
                stack.append(total)
            else:
                stack.append(t)
        return int(stack.pop())