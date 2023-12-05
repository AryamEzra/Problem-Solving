class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        
        total_dist = sum(distance)
        sum_dist_cw = sum(distance[start:destination])
        sum_dist_ccw = total_dist - sum_dist_cw
        
        output = min(sum_dist_cw,sum_dist_ccw)
        return output

    
        