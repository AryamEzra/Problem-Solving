class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row_max = [0] * n
        col_max = [0] * m
        for i in range(n):
            for j in range(m):
                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])
        count = 0
        for i in range(n):
            for j in range(m):
                add = min(row_max[i], col_max[j])
                count += (add - grid[i][j])
        return count

        