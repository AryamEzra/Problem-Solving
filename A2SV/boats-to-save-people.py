class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #time:O(nlogn)
        #space: O(1)

        boats = 0
        people.sort()
        i = 0
        p1 = len(people) - 1 
        while i <= p1:
            if people[i] + people[p1] <= limit:
                boats += 1
                i += 1
                
            else:
                boats += 1
            p1 -= 1
        return boats

        