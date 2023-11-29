class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ans = []
        total = 0
        i = 0
        
        while 3**i <= n:
            ans.append(3**i)
            #print(ans)
            i += 1
        ans = ans[::-1]
        for i in range(len(ans)):
            if total <= n:
                total += ans[i]
                if total == n:
                    return True
                    break
            if total > n:
                total -= ans[i]
        if total != n:
            return False
            
            
           


        

            

        