class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #time: O(n**2)
        #space: O(n)

        n = len(nums)
        s = len(set(nums))
        count = 0
        for i in range(n):
            seen = set()
            for j in range(i,n):
                seen.add(nums[j])
                if len(seen) == s:
                    count += 1
                elif len(seen) > s:
                    break
        return count