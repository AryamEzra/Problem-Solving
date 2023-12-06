class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                good_num = num[i:i+3]
                if good_num > ans:
                    ans = good_num
        return ans 
        
        