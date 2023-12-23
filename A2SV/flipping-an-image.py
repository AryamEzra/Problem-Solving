class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(image)):
            image[i] = image[i][::-1]
            ans.append(image[i])
        for i in range(len(ans)):
            for j in range(len(ans)):
                if ans[i][j] == 0:
                    ans[i][j] = 1
                else:
                    ans[i][j] = 0
        return ans

        