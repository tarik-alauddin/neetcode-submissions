# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root: Optional[TreeNode]):

            if not root:
                return 0, 0

            # traverse
            leftHeight, leftDiameter = dfs(root.left)
            rightHeight, rightDiameter = dfs(root.right)

            #calculate
            height = 1 + max(leftHeight, rightHeight)
            diameter = max(leftHeight + rightHeight, leftDiameter, rightDiameter)

            return height, diameter

        height, diameter = dfs(root)
        return diameter