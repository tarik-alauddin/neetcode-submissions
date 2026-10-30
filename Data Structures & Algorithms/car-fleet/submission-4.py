class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_t = [] # [(position, time to target)]

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            p_t.append((position[i], time))

        p_t.sort(reverse=True) # descending order by position eg. 7, 4, 1, 0

        stack = []
        for p, t in p_t:
            if not stack:
                stack.append(t)
            elif stack[-1] < t:
                stack.append(t)

        return len(stack)