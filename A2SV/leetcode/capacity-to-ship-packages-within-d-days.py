class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        w = len(weights)
        
        def minimum_weight(mid):
            summ = 0
            count = 1
            for i in range(w):
                if summ + weights[i] > mid:
                    summ = 0 
                    count += 1
                summ += weights[i]
            if count > days:
                return False
            return True
        
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = l + (r-l) // 2
            if minimum_weight(mid): # return True
                r = mid - 1
            else:
                l = mid + 1

        return l   

        