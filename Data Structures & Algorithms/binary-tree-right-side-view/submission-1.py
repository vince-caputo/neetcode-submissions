# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        res = [root.val]
        dq = deque([root])
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
            if dq:
                res.append(dq[-1].val)
        return res