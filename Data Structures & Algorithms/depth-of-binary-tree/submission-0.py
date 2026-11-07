# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            maxleft = dfs(root.left)+1
            maxright = dfs(root.right)+1

            return max(maxleft, maxright)

        return dfs(root)
        
        

            