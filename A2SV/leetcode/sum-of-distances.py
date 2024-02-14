class Solution:
    def distance(self, nums: List[int]) -> List[int]:
    
        if len(set(nums)) == len(nums): 
            return [0]*len(nums)

        ans = [0]*len(nums)
        store = {}
        
        for i, num in enumerate(nums):
            if num not in store:
                store[num] = []
                store[num].append(i)
            else:
                store[num].append(i)
        #print(store)

        for num, val in store.items():
            suffix_sum = sum(val)
            prefixSum = 0
            s = len(val)
            p = 0
            for i in val:
                prefixSum += i
                p += 1
                suffix_sum -= i
                s -= 1
                ans[i] = (p*i - prefixSum) + (suffix_sum - s*i)

        return ans
                

        


        