# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def traversal(root):
            nonlocal ans
            if root is not None:
                traversal(root.left)
                if root.val >= low and root.val <= high:
                    ans += root.val
                traversal(root.right)
        traversal(root)
        return ans