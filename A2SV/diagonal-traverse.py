class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # time complexity: o(n*m)
        # space complexity: 0(n)

        store = defaultdict(list)
        r = len(mat)
        c = len(mat[0])
        for row in range(r):
            for col in range(c):
                store[row+col].append(mat[row][col])
        s = len(store)
        ans=[]
        for i in range(s):
            if i % 2 == 0:
                for j in range(len(store[i])-1,-1,-1):
                    ans.append(store[i][j])
            else:
                for j in range(len(store[i])):
                    ans.append(store[i][j])
        return ans
        
            

        