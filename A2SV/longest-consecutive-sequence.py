class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_count = 0

        for num in nums:
            if (num-1)  not in numset:
                cur_count = 0

                #increments cur_count as long as the next consecutive number (n + cur_length) is present in the numset 
                #This loop counts the length of the consecutive sequence starting from num.
                while (num + cur_count) in numset: 
                    cur_count += 1
                max_count = max(max_count, cur_count)
                
        return max_count

        