# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def compare (root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2) or root1.val != root2.val:
                return False

            left = compare(root1.left, root2.right)
            right = compare(root1.right, root2.left)
            return left and right

        return compare(root.left, root.right)

