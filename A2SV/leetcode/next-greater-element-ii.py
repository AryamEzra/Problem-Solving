class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        greater = [-1] * len(nums)
        new = []
        n = len(nums)

        for i in range(len(nums)* 2):
            while stack and nums[stack[-1]] < nums[i % n] :
                top = stack.pop()
                greater[top] = nums[i % n]
                
            stack.append(i % n)

        return greater
        