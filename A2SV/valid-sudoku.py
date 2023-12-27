class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #time: O(n**4)
        #space: O(n)

        row = len(board)
        col = len(board[0])

        check_row = True
        check_col = True
        check3 = True

        for i in range(row):
            seen_row = set()
            for j in range(col):
                c = board[i][j]
                if c == ".":
                    continue
                elif c not in seen_row:
                    seen_row.add(c) 
                elif c in seen_row:
                    check_row = False
                    break
            

        for i in range(col):
            seen_col = set()
            for j in range(row):
                c = board[j][i]
                if c == ".":
                    continue
                elif c not in seen_col:
                    seen_col.add(c) 
                elif c in seen_col:
                    check_col = False
                    break
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen_three = set()
                for r in range(0, 3):
                    for d in range(0, 3):
                        c = board[i+r][j+d]
                        if c == ".":
                            continue
                        elif c not in seen_three:
                            seen_three.add(c) 
                        elif c in seen_three:
                            check3 = False
                            break
        if check_row == True and check_col == True and check3 == True:
            return True
        else:
            return False
        
        