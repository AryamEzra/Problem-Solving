class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        threes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    threes[(i//3, j//3)].add(board[i][j])
                            
        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r+1, 0)
            if board[r][c] != ".":
                return backtrack(r, c+1)

            for i in range(1, 10):
                num = str(i)
                if num not in rows[r] and num not in cols[c] and num not in threes[(r//3,c//3)]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    threes[(r//3,c//3)].add(num)

                    if backtrack(r, c+1):
                        return True
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    threes[(r // 3, c // 3)].remove(num)
            return False
        backtrack(0,0) 
                    


                
                
        