class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0"  in [num1, num2]:
            return "0"
            
        res = [0] * (len(num1)+len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        # beacause when we muliple we satrt from the end of the digit we need to reverse inorder to take the ones place

        for i in range(len(num1)):
            for j in range(len(num2)):

                #multiplying ht e ones place of both numbers
                digit = int(num1[i]) * int(num2[j]) 

                #if the number is a two digit number the max being 9 * 9 = 81, we store the value on the sum of theier indexes and inorder to get the one's we place we mod by 10 and inorder to get the carry we will add onto the next number we will floor divide by 10 and store that on the palce next to it

                res[i+j] += digit
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] = (res[i+j] % 10)    
                
        
        # we need to reverse the answer beacuse have been calualting froom the ones postion meaning the end and we want to remove leading zeros remaning when we first intiazted our array

        res, start = res[::-1], 0
        while start < len(res) and res[start] == 0:
            start += 1
        
        res = map(str, res[start:])
        return "".join(res)