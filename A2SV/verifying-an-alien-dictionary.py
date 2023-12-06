class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #time complexity O(n.m) where n is the no of words and m is the no of chara 
        #thereforet hr total number of charac inside the words
        #create a map that will map the char(key) to the index(value) for order
        lookup = {char:index for index, char in enumerate(order)}

    
        check = []
        for word in words:
            arr = []

            #go through all the characters in words
            for char in word:

                #append the indexes of those characters
                arr.append(lookup[char])

            #append the list of numbers to the check list so that we can start comparing it 
            check.append(arr)
        
        for i in range(1, len(words)):
            if check[i-1] > check[i]:
                return False
        return True

        