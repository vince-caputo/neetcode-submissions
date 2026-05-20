# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def getDepth(root):
            if not root:
                return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        
        not_including_root = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        if root.left and root.right:
            return max(not_including_root, getDepth(root.left) + getDepth(root.right))
        return max(getDepth(root) - 1, not_including_root)




