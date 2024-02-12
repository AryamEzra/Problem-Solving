class Solution:
    def numberOfWays(self, s: str) -> int:
        #time: O(n)
        #space: O(n)

        #1 -> first char 
        #01 -> second char
        #101 -> total char 

        #0 -> first char 
        #10 -> second char
        #010 -> total char 

        
        ans = 0
        before = [0] * 2
        after = [0] * 2
        after[0] = s.count('0')
        after[1] = len(s) - after[0]

        for c in s:
            num = int(c)
            after[num] -= 1
            if num == 0:
                ans += before[1] * after[1]
            else:
                ans += before[0] * after[0]
            before[num] += 1
                

        return ans

        
        # #for 1:
        # one = s.count("1")
        # partner_one = s.count("01")
        # total_one = (one * partner_one) - partner_one
        # print(total_one)

        # #for 0:
        # zero = s.count("0")
        # partner_zero = s.count("10")
        # total_zero = (zero * partner_zero) - partner_zero
        # print(total_zero)
        # return total_one + total_zero
