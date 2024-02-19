class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        #time: O(n)
        #space: O(n)

         
        set_nums = len(set(nums))
        ans = 0
        seen = defaultdict(int)
        left = 0
        for right in range(len(nums)):
            seen[nums[right]] +=1
            while len(seen) == set_nums :
                ans += len(nums) - right
                seen[nums[left]] -=1
                if not seen[nums[left]]:
                    del seen[nums[left]]
                left +=1
        return ans