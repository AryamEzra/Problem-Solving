class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n+1)
        result = []
        
        for start,end,direc in shifts:
            if direc == 1:
                prefix[start] += 1
                prefix[end+1] -= 1
            else:
                prefix[start] -= 1
                prefix[end+1] += 1
                
        for index in range(1,n+1):
            prefix[index] += prefix[index -1]
        
        for index, shift in enumerate(prefix[:-1]):
            char_position = ascii_lowercase.index(s[index])
            shifted = (shift + char_position) % 26
            shifted_char = ascii_lowercase[shifted]
            result.append(shifted_char)
        return "".join(result)
            
            