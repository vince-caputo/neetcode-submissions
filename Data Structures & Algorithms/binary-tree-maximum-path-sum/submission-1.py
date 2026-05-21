# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -float('inf')

        def maxRunDown(root):
            if not root:
                return 0
            
            leftMax = maxRunDown(root.left)
            rightMax = maxRunDown(root.right)
            return root.val + max(leftMax, rightMax, 0)

        
        return max(self.maxPathSum(root.left), self.maxPathSum(root.right), max(maxRunDown(root.left),0) + root.val + max(maxRunDown(root.right), 0))