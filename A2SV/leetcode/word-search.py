class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        w = len(word)
        direction = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        def backtrack(idx, i, j):
            if idx == w:
                return True

            for x,y in direction:
                posx, posy = i+x, j+y

                if 0 <= posx < n and 0 <= posy < m:
                    if board[posx][posy] == word[idx] and (posx,posy) not in visited:
                        visited.add((posx,posy))
                        if backtrack(idx+1, posx, posy):
                            return True
                        visited.remove((posx,posy))            
                

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((i,j))
    
                    if backtrack(1, i, j):
                        return True
                    visited.remove((i,j))


        return False


    
        