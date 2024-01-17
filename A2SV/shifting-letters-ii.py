class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        #time:
        #space:
        
        string = "abcdefghijklmnopqrstuvwxyz"
        n = len(s)
        prefix_sum = [0] * (n + 1)

        char = []
        res = []
        
        ans = []
        #prefix_sum[end+1] - because we want to inclue the end so we need to do end + 1
        for start, end, dire in shifts:
            if dire == 1:
                prefix_sum[start] += 1
                prefix_sum[end+1] -= 1
            else:
                prefix_sum[end+1] += 1
                prefix_sum[start] -= 1
        

        for idx in range(1, n+1):
            prefix_sum[idx] += prefix_sum[idx - 1]
        
        for char in s:
            if char in string:
                res.append(string.index(char))

        pos = []
        x = 0
        for i in range(len(res)):
            x = res[i] + prefix_sum[i]
            pos.append(x)

        for k in pos:
            ans.append(string[k % 26])
        final = "".join(ans)
        return final
         



        # for i in range(len(s)):
        #     char.append(ord(s[i]))
        # char.append(0)
        
        # for i in range(len(char)):
        #     summ = prefix_sum[i] + char[i]
        #     res.append(summ)
        # print(res)
        # for j in range(len(res)):
        #     if res[j] <= 122 and res[j] >= 97:
        #         word.append(chr(res[j]))
        # return "".join(word)  


        
        
        
            
