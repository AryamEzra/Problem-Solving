class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        left_sum = 0
        right_sum = 0
        left, right = 0, 0
        while left < len(mat):
            while right < len(mat):
                left_sum += mat[left][right]
                right += 1
                left += 1
        r = 0
        c = len(mat) - 1
        while r < len(mat):
            while c >= 0:
                right_sum += mat[r][c]
                r += 1
                c -= 1
        if len(mat) % 2 == 0:
            return(left_sum + right_sum)
        else:
            return(left_sum + right_sum - mat[len(mat)//2][len(mat)//2])
        

        