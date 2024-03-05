class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        letters = {"2": ["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], 
                   "5": ["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"],
                   "8": ["t", "u", "v",], "9":[ "w", "x", "y", "z"] }
        d = len(digits)
        x = ""
        def backtrack(idx, combo):
            nonlocal x
            if len(combo) == d:
                x = "".join(combo[:])
                ans.append(x)
                return 
            if len(combo) > d:
                return
            for i in letters[digits[idx]]:
                combo.append(i)
                backtrack(idx+1, combo)
                combo.pop()
        if not digits:
            return []
        backtrack(0, [])
        return ans
                

        
        