class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #time: O(nlogn)
        #space: o(1)

        costs.sort()
        output = 0
        if costs[0] > coins:
            return 0
        
        for i in range(len(costs)):
            if coins >= costs[i]:
                coins -= costs[i]
                output += 1
        return output


        