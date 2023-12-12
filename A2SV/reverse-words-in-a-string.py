class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        words = s.split(" ")
        print(words)

        arr = []
        for i in range(len(words)):
            if words[i] != "":
                arr.append(words[i])
        
        arr = arr[::-1]
        
        return " ".join(arr)

        