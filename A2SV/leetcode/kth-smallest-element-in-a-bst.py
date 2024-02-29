# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def makelist(root):
            if not root:
                return []
            left = makelist(root.left)
            right = makelist(root.right)
            ans = []
            ans.append(root.val)
            ans.extend(left)
            ans.extend(right)
            return ans
        res = makelist(root)
        res.sort()
        return res[k-1]
        