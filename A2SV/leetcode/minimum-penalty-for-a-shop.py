class Solution:
    def bestClosingTime(self, customers: str) -> int:
        c = len(customers)
        sumy = customers.count("Y")
        prefix_sum = [0]
        postfix_sum = [0]
        ans = 0
        for i in range(c):
            if customers[i] == "N":
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])
        
        for i in range(c-1, -1, -1):
            if customers[i] == "Y":
                postfix_sum.append(postfix_sum[-1] + 1)
            else:
                postfix_sum.append(postfix_sum[-1])
        postfix_sum[:]  = postfix_sum[::-1]
        minn = float('inf')
        for i in range(c+1):
            res = (prefix_sum[i] + postfix_sum[i])
            tmp = minn
            minn = min(res, minn)
            if tmp != minn:
                ans = i
        
        return ans