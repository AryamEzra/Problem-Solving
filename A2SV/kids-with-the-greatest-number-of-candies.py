class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        max_ele = max(candies)
        for i in range(len(candies)):
            ans = candies[i] + extraCandies
            
            if ans >= max_ele:
                arr.append(True)
            else:
                arr.append(False)
        return arr


        