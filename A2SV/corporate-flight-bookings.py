class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #time: O(n)
        #space: O(n)

        arr = [0] * (n+2)
        cur = 0
        
        for first,last,seats in bookings:
            arr[first] += seats
            arr[last + 1] -= seats
        
        for i in range(1, len(arr)):
            arr[i] += arr[i-1] 

        del arr[0]
        del arr[-1]
        
        return arr
        