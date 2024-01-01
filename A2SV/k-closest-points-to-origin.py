class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #time:O(nlogn)
        #space:O(n)

        #if you make ans a dictionary it will not work beacuse it will return a tuple so make a list and that stores values as a tuple like ans = [], ans.append((dist, [x,y]))

        ans = []
        res = []
        for x,y in points:
            dist = (x**2) + (y**2)
            ans.append((dist, [x,y]))

        sorted_ans = sorted(ans) #this sorts the answer by the first element


        count = 0
        for key, val in sorted_ans:
            res.append(val)
            count += 1
            if count == k:
                break
        return res   
        
        
            
        