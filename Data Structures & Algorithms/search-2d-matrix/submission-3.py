class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        i = 0

        print("len: ", len(matrix))

        # find first row that has last val GT target
        while i < len(matrix):
            print("i: ", i)
            if matrix[i][-1] >= target:
                row = i
                break
            i += 1

        if row == -1:
            return False

        L = 0
        R = len(matrix[row])-1

        while L <= R:
            mid = (L+R)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                L = mid + 1
            elif matrix[row][mid] > target:
                R = mid - 1
        
        return False