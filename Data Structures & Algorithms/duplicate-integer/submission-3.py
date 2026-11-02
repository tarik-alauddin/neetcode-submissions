class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for i in range(len(nums)):
            m[nums[i]] += 1

            if m[nums[i]] > 1:
                return True

        return False