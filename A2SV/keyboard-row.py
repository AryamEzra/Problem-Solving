class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        res = []
        for word in words:
            lower_word = word.lower()

            #set(lower_word) & set(row1) == set(lower_word) this has two parts
            #set(lower_word) & set(row1) - can instersect two sets using "&"
            #set(lower_word) & set(row1) == set(lower_word if check all the char in thw lower_case to be found in row 1 then it wil return true and append that word onto our result 
            if ((set(lower_word) & set(row1)) == set(lower_word)) or ((set(lower_word) & set(row2)) == set(lower_word)) or ((set(lower_word) & set(row3)) == set(lower_word)):
                res.append(word)
        return res
