# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        level = defaultdict(list)
        
        def traverse(cur_node, depth):
            if cur_node is None:
                return 
            level[depth].append(cur_node.val)
            
            traverse(cur_node.left, depth+1)
            traverse(cur_node.right, depth+1)
        traverse(root, 0)
        for key, val in level.items():
            if key % 2: #if key is odd
                ans.append(val[::-1])
            else:
                ans.append(val)
        return ans
        