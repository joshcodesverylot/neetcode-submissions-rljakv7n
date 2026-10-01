class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ps = []
        for i in range(len(position)):
            ps.append([position[i], speed[i]])
        ps = sorted(ps, key=lambda ps: ps[0])
        for l in range(len(ps) - 1, -1, -1):
            pos, speed = ps[l]
            time = (target - pos)/ speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)