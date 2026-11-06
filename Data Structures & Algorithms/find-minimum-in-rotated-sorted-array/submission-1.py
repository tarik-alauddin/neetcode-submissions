class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        res = nums[0]

        while L <= R:
            # if L < R ever, we are in reg sorted order
            if nums[L] < nums[R]:
                res = min(res, nums[L])
                break

            mid = (L + R) // 2
            res = min(res, nums[mid])

            # if mid GTE L then we have the min on left
            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1

        return res