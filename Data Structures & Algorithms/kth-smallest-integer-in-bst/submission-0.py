# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def getNumNodes(root):
            if not root:
                return 0
            
            return 1 + getNumNodes(root.left) + getNumNodes(root.right)

        leftNodes = getNumNodes(root.left)

        if leftNodes >= k:
            return self.kthSmallest(root.left, k)
        
        if leftNodes == k - 1:
            return root.val

        return self.kthSmallest(root.right, k - leftNodes - 1)