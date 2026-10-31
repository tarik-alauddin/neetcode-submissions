class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(numbers)):
            if numbers[i] in m:
                return [m[numbers[i]] + 1, i + 1]

            num = target - numbers[i]
            
            m[num] = i