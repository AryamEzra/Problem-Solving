class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arrows = 0 
        points.sort()
        minn = float('-inf')
        print(points)
        for i in range(len(points)):
            if points[i][0] <= minn and minn <= points[i][1]:
                minn = min(minn, points[i][1])

            elif points[i][0] <= minn and minn > points[i][1]:
                minn = min(minn, points[i][1])
                 
            else:
                minn = max(minn, points[i][1])
                arrows += 1
            
        return arrows

        