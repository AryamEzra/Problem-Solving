class Solution:
    def printVertically(self, s: str) -> List[str]:
        output = []
        string = s.split(" ")
        max_length = max(len(word) for word in string)

        for i in range(max_length):
            vertical_word = ""

            for word in string:
                if i < len(word):
                    vertical_word += word[i]
                else:
                    vertical_word += " "
            output.append(vertical_word.rstrip())
        return output