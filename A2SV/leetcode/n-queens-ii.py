class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        right_diagonal = set()
        left_diagonal = set()
        rowy = []
        board = [["." for _ in range(n)] for _ in range(n)]
        print(board)
        def chess(row):
            if row == n:
                fake =[]
                for i in board:
                    fake.append("".join(i))
                rowy.append(fake)
                return
            for i in range(n):
                if i in cols or i+row in right_diagonal or row-i in left_diagonal:
                    continue
                board[row][i] = "Q"
                cols.add(i)
                right_diagonal.add(row+i)
                left_diagonal.add(row-i)

                chess(row + 1)

                board[row][i] = "."
                print(cols)
                cols.remove(i)
                right_diagonal.remove(row+i)
                left_diagonal.remove(row-i)
                
        chess(0)
        return len(rowy)