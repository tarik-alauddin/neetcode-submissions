class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                # we are at start of sequence
                val = num
                length = 0
                while val in numSet:
                    length += 1
                    val += 1
                    longest = max(longest, length)

        return longest