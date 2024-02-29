# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__ (self):
    #     self.ans = []
    #     self.freq = {}
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
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
        count = Counter(res)
        output = []
        max_freq = 0
        for val in count.values():
            if val > max_freq:
                max_freq = val
        for key,val in count.items():
            if max_freq == val:
                output.append(key)
        return output


        
        # def solve(num):
        #     if num in self.freq:
        #         self.freq[num] += 1
        #     else:
        #         self.freq[num] = 1

        # print(self.freq) 
        # return solve(root.val)
        
     