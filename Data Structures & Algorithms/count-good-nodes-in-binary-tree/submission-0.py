# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesWithRunningMax(root, runningMax):
            if not root:
                return 0

            if root.val >= runningMax:
                return 1 + goodNodesWithRunningMax(root.left, root.val) + goodNodesWithRunningMax(root.right, root.val)
            return goodNodesWithRunningMax(root.left, runningMax) + goodNodesWithRunningMax(root.right, runningMax)
        
        return goodNodesWithRunningMax(root, -float('inf'))
        
