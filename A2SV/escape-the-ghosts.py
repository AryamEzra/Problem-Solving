class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        check = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            dist = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if dist <= check:
                return False
        return True
             
        
        
        