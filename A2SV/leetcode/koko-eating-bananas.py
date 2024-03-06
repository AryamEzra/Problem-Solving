class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p = len(piles)
        def minimum_integer(mid):
            count = 0
            for i in range(p):
                count += ceil(piles[i] / mid)
            if count > h:
                return False
            return True
        l = 1
        r = max(piles)
        print(3//6)
        while l <= r: # mid is the speed, when they pass one another that is the minimum so we return left
            mid = (l + r) // 2
            if minimum_integer(mid): # return True
                r = mid - 1
            else:
                l = mid + 1
            
        return l
             


        


        