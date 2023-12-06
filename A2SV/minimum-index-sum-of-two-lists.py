class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_ij = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i + j < min_ij:
                        min_ij = i + j 
                        ans = [list1[i]]
                    elif i + j == min_ij:
                        ans.append(list1[i])

        return ans
        '''
        ans = []
        min_ij = float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    min_ij = i + j 
                    ans = list1[i])
                    sum_ij.append(i+j)
                else:
                    j += 1
            i += 1
        print(ans)
        print(sum_ij)
        min_ij = min(sum_ij)
        print(min_ij)
        final_ans = []

        for i in range(len(ans)):
            if i <= min_ij:
                final_ans.append(ans[i])
        return final_ans
        '''
        