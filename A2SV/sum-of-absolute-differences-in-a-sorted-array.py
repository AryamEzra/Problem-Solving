class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        #time: O(n)
        #space: O(n)

        ans = []
        total = sum(nums)

        prefix_sum = 0
        n = len(nums)
        for idx, num in enumerate(nums):
            suffix_sum = total - num - prefix_sum
            left_side = idx
            right_side = n - idx - 1

            sol = ((left_side * num) - prefix_sum) + (suffix_sum - (right_side * num))
            ans.append(sol)

            prefix_sum += num
        return ans


        '''
        #Brute force
        #time: O(n**2)
        #space: O(n)

        n = len(nums)
        ans = []
        for i in range(n):
            diff = nums[i]
            abs_ans = 0
            for j in range(n):
                abs_ans += abs(diff - nums[j])
            ans.append(abs_ans)
        return ans
        '''