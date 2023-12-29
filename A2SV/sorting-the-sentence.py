class Solution:
    def sortSentence(self, s: str) -> str:
        #time:O(n) -> O(9)
        #space:O(n) -> O(9)

        dic = {}
        ans = []
        last_idx = []

        s = list(s.split(" "))
        
        for i in range(len(s)):
            last_idx.append(int(s[i][-1]))
            dic[int(s[i][-1])] =s[i][:-1]
        sorted_arr = sorted(last_idx)
        for num in sorted_arr:
            ans.append(dic[num])

            
        return " ".join(ans)

        