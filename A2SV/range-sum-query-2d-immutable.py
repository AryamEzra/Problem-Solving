class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [[0] * (len(matrix[0])+ 1) for r in range(len(matrix)+1)]
        
        for r in range(len(matrix)):
            prefix = 0
            for c in range(len(matrix[0])):
                prefix += matrix[r][c]
                above = self.prefix_sum[r][c+1]
                self.prefix_sum[r+1][c+1] = prefix + above

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        bottom_right = self.prefix_sum[r2][c2]
        above = self.prefix_sum[r1-1][c2]
        left = self.prefix_sum[r2][c1-1]
        top_left = self.prefix_sum[r1-1][c1-1]

        return bottom_right + top_left - above - left       

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)