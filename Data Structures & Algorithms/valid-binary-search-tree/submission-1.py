# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, runningMax, runningMin):
            if not root:
                return True
            
            if root.val >= runningMax or root.val <= runningMin:
                return False

            return isValid(root.left, min(runningMax, root.val), runningMin) and isValid(root.right, runningMax, max(runningMin, root.val))

        return isValid(root, float('inf'), -float('inf'))