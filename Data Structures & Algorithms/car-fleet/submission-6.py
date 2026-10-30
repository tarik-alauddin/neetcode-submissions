class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_t = [] # [(position, time to target)]

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            p_t.append((position[i], time))

        p_t.sort(reverse=True) # descending order by position eg. 7, 4, 1, 0

        stack = []
        slowest_time = p_t[0][1]
        count = 1
        for p, t in p_t:
            if slowest_time < t:
                count += 1
                slowest_time = t

        return count