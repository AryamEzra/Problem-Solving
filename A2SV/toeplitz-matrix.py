class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #top left to bottom right
        for row in range(len(matrix)):
            for col in range(1,len(matrix[0])):
                if row > 0 and col > 0 and matrix[row][col] != matrix[row-1][col-1]:
                    return False
        
        return True