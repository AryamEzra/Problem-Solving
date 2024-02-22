class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #time: O(n)
        #space: O(n)

        ans = float('inf')
        target = 0

        n = len(nums)
        for i in range(n):
            target = (target + nums[i]) % p
        if target == 0:
            return 0
        
        store = {0:-1} # cur_rem : idx
        cur_rem = 0

        for i in range(n): # i = idx
            cur_rem = (cur_rem+ nums[i]) % p
            
            find = store.get((cur_rem - target + p) % p)
            if find is not None:
                ans = min(ans, i - find)
            if cur_rem >= target:
                find = store.get((cur_rem - target) % p)
                if find is not None:
                    ans = min(ans, i - find)
            store[cur_rem] = i
        
        if ans >= n:
            return -1
        else:
            return ans


