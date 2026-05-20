# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        dq = deque([root])
        res = []
        while True:
            row = []
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    row.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    dq.append(None)
                    dq.append(None)

            res.append(row)
            if dq == deque([None] * len(dq)):
                return res