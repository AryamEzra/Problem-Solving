# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.pans = []
        self.qans = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            self.isSameTree(p.left, q.left)
            self.pans.append(p.val)
            self.qans.append(q.val)
            self.isSameTree(p.right, q.right)
        if p is not None and q is None:
            self.pans.append(p.val)
            self.qans.append(None)

        if p is None and q is not None:
            self.pans.append(None)
            self.qans.append(q.val)

        return self.pans == self.qans
            
        