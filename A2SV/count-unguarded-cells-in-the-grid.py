class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #time:O(n**3)
        #space:O(n)
        #n ->  col
        #m -> row
       
        res = 0
        grid = [[0 for _ in range(n)] for j in range(m)]
        
        
        for x,y in guards:
            grid[x][y] = "G"
            
        for x,y in walls:
            grid[x][y] = "W"   
        
        for x,y in guards:
            tmpx = x
            tmpy = y

            # + row
            x += 1
            while x < m and grid[x][y] != "W" and grid[x][y] != "G":
            
                grid[x][y] = "X" 
                x += 1

            x = tmpx

            # - row
            x -= 1
            while x >= 0 and grid[x][y] != "W" and grid[x][y] != "G":
            
                grid[x][y] = "X" 
                x -= 1 
                   
            x = tmpx

            # + col
            y += 1
            while y < n  and grid[x][y] != "W" and grid[x][y] != "G":
                
                grid[x][y] = "X" 
                y += 1
                
            y = tmpy

            # - col
            y -= 1
            while y >= 0 and grid[x][y] != "W" and grid[x][y] != "G":
                grid[x][y] = "X" 
                y -= 1 
                   
            y = tmpy
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res += 1
        return res 

            



        
        