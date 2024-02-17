class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # time: O(n)
        # space: O(1)
        ans = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 1:
                ans += 1
                target -= 1
            if target % 2 == 0:
                ans += 1
                maxDoubles -= 1
                target = target // 2
        ans += target - 1
        return ans 
            