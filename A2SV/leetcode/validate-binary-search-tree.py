# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def work(root,before, after):
            if root is None:
                return True
            if root.val >= after or root.val <= before:
                return False
            return work(root.left, before, root.val) and work(root.right, root.val, after)
        return work(root, float('-inf'), float('inf'))
 
            
                



        