class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        #each time we see the number that is already in our diciotnary we want to shift the left pointer and calucalte the sum starting from that pointer but we also want to subrate the value of the number we just saw and then we shift the left pointer

        seen = {} #val(integer) : index

        maxx = 0
        output = 0
        left = 0

        for idx,val in enumerate(nums):
            if val in seen:
                while left < seen[val] + 1:
                    maxx -= nums[left]
                    left += 1
            
            seen[val] = idx
            maxx += val
            output = max(maxx, output)

        return output



        