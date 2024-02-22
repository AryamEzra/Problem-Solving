class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        new = []
        greater = [-1] * len(nums2)
        store = {}
        ans = [0]*len(nums1)
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                top = stack.pop()
                greater[top] = i
            stack.append(i)

        for i in greater:
            if i == -1:
                new.append(i)
            else:
                new.append(nums2[i])
                
        for i in range(len(nums2)):
            store[nums2[i]] = new[i]
        
        for i in range(len(nums1)):
            ans[i] = store[nums1[i]]
        return ans
           
            

            
        