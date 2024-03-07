class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        max_radius = float('-inf')
        h = len(houses)
        check = len(heaters)
        for i in range(h):
            idx = bisect_left(heaters, houses[i])
            if idx <= 0:
                cur = abs(heaters[0] - houses[i])
                max_radius = max(max_radius, cur)
            if idx >= check:
                cur = houses[i] - heaters[-1]
                max_radius = max(max_radius, cur)
            else:
                cur1 = abs(heaters[idx] - houses[i])
                cur2 = abs(heaters[idx-1] - houses[i])
                cur = min(cur1, cur2)
                max_radius = max(max_radius, cur)
        return max_radius
            
         