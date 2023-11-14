class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boats = 0 #res
        
        while left <= right:
            remain = limit - people[right]
            right -= 1
            boats += 1
            
            if left <= right and remain >= people[left]:
                left += 1
        return boats
                