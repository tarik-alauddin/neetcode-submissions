class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0: # will never sum to 0
                break

            if i > 0 and n == nums[i - 1]: 
                continue

            left = i + 1
            right = len(nums)-1

            while left < right:
                threeSum = n + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1

        return res

