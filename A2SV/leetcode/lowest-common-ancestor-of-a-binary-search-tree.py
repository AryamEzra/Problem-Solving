# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def move(cur):
            if not cur:
                return 
            if cur == p or cur == q:
                return cur
            left = move(cur.left)
            right = move(cur.right)

            if not left:
                return right
            if not right:
                return left
            else:
                return cur
        return move(root)

        