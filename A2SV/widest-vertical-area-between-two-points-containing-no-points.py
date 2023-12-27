class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_dist = -float('inf')
        first = []
        for i in range(len(points)):
            first.append(points[i][0])
        first.sort()
        for i in range(len(first)-1):
            cur_dist = first[i+1] - first[i]
            max_dist = max(cur_dist, max_dist)
               
        return max_dist
            
        