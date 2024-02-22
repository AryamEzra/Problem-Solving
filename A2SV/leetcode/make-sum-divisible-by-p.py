class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #time:
        #space:

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




        # if sum(nums) % p == 0:
        #     return 0
        # summ = sum(nums)
        # div = summ // p
        # find = summ -  div
        
        # cur_sum = 0
        # rem_lst = [0]
        # for i in range(len(nums)):
        #     cur_sum += nums[i]
        #     rem_lst.append(cur_sum % p)
        
        # count = 0
        # for i in range(len(rem_lst)-1):
        #     k = rem_lst[i+1] - rem_lst[i]
        #     if  k % p == find:
        #         count += 1
        # return count

    

                
        # count = 0
        # cur  = 0
        # dic = {0:1}
        # for i in range(len(nums)):
            
        #     cur += nums[i]
        #     rem = cur % p
        #     if rem in dic.keys():
        #         count += dic[rem]
            
        #     dic[rem] = dic.get(rem, 0) + 1
        # print(dic)
        # return count


        # dic = {}
        # prefix_sum = []
        # ans = []
        # summ = 0
        # count = 0
        # for i in range(len(nums)):
        #     summ += nums[i]
        #     prefix_sum.append(summ)
        #     ans.append(summ % p)
        # print(ans)
        # for i in range(len(ans)):
        #     if p - ans[i] == nums[i]:
        #         count += 1
        # return count

        