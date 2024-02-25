class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #decreasing montonic deque - to remove and add elements in O(1) time
        ans = []
        left = 0
        queue = deque() # storing indexes

        for right in range(len(nums)): 
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()
            if (right + 1) >= k:
                ans.append(nums[queue[0]]) 
                left += 1
        return ans
        