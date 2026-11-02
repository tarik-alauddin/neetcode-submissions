class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        L = 0
        maxlen = 0

        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            chars.add(s[R])
            maxlen = max(maxlen, R - L + 1)

        return maxlen