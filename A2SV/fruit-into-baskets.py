class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #time: O(n)
        #space: O(n)

        pick = {}
        total = 0
        res = 0
        left = 0
        
        for right in range(len(fruits)):
            pick[fruits[right]] = pick.get(fruits[right], 0) + 1
            while len(pick) > 2:
                pick[fruits[left]] -= 1
                if pick[fruits[left]] == 0:
                    del pick[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
            total = max(total, res)

        return total
        