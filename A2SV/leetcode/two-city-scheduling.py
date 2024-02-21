class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_sum = 0
        costs.sort(key = lambda x : x[0] - x[1])
        print(costs)
        n = len(costs) // 2
        for i in range(n):
            x = costs[i][0]
            min_sum += x
        for i in range(n, len(costs)):
            y = costs[i][1]
            min_sum += y
        return min_sum

        
        