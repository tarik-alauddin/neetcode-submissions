class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxlen = 0
        freq = [0] * 26
        maxfreq = 0

        for R in range(len(s)):
            # calculate the frequency
            r = ord(s[R]) - ord('A')

            freq[r] += 1

            maxfreq = max(maxfreq, freq[r])

            while (R - L + 1) - maxfreq > k:
                freq[ord(s[L]) - ord('A')] -= 1
                L += 1

            maxlen = max(maxlen, R - L + 1)

        return maxlen