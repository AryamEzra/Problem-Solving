class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        seen = set()

        for front, back in zip(fronts, backs):
            if front == back:
                seen.add(front)
        
        min_num = float('inf')
        for num in fronts:
            if num not in seen:
                min_num = min(min_num, num)
        
        for num in backs:
            if num not in seen:
                min_num = min(min_num, num)
        
        return min_num if min_num != float('inf') else 0