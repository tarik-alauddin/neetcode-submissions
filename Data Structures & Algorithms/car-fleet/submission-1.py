class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = []

        for i in range(n):
            pairs.append([position[i], speed[i]])
        
        pairs.sort(reverse=True)
        
        stack = []
        for pos, speed in pairs:
            stack.append((target-pos)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
