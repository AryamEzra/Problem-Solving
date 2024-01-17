class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #sum of ele to the right must equal to the sum of ele to the left and it        shouldn't include that element
        #we use prefix sum (left), suffix sum(from the right) and two pointers
        #if thery are == to one another and not equal to 0

        #time: O(n)
        #space: O(1)

        total = sum(nums)

        leftsum = 0
        for i in range(len(nums)):
            rightsum = total - leftsum - nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1 

            
        

        