class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort()
        q = collections.deque(piles) 
        #to keep track
        while len(q) > 0:
            q.popleft()
            q.pop()
            count += q[-1]
            q.pop()
            
        return count
        