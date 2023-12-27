class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        #time: O(m*n)
        #space: O(1)

        ans = 0

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                ans = max(ans, (grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1] + grid[row][col] + grid[row+1][col] + grid[row+1][col-1] + grid[row+1][col+1]))
                
        return ans

                

        
        