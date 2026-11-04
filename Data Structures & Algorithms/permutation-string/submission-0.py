class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1 = [0] * 26
        for s in s1:
            f1[ord(s) - ord('a')] += 1

        f2 = [0] * 26
        L = 0

        for R in range(len(s2)):
            f2[ord(s2[R]) - ord('a')] += 1

            while R - L + 1 > len(s1):
                f2[ord(s2[L]) - ord('a')] -= 1
                L += 1

            if f1 == f2:
                return True

        return False