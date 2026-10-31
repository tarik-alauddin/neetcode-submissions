class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort piles in ascending order
        piles.sort()
        minK = 0

        L = 1
        R = piles[-1]

        while L <= R:
            k = (L + R) // 2

            if k == 0:
                return minK

            tempH = h

            for i in range(len(piles)):
                tempH -= math.ceil(piles[i]/k)

            if tempH >= 0:
                minK = k
                R = k - 1
            elif tempH < 0:
                L = k + 1

        return minK
