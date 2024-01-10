class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #time:
        #space:
        
        s_list = [char for char in s]
        p_list = [char for char in p]
        x = sorted(p)
        len_p = len(p)
        ans = []
        i = 0
        while i < len(s) and len_p <= len(s):
            check = sorted(s[i:len_p])
            if check == x:
                ans.append(i)
            i += 1
            len_p += 1
        return ans

            
        


        