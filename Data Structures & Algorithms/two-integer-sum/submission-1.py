class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}

        for i in range(len(nums)):
            if nums[i] in l:
                return [l[nums[i]], i]

            val = target - nums[i]
            l[val] = i