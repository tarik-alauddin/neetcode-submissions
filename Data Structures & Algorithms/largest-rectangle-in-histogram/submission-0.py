class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # area = height * width
        # largest area will be the tallest height over the longest width
        
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((start, h))

        # we have maxArea and potentially items still on the stack
        # items on stack extend to len(heights)
        
        n = len(heights)
        while stack:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (n-index))

        return maxArea