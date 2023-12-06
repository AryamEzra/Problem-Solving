class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        check = floor(n/3)
        count = Counter(nums)
        res = []
        
        for i in count:
            if count[i] > check:
                res.append(i)
        return res


            
                
            


        
    
        