class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ans = []
        count = [0] * 1001

        for num in arr1:
            count[num] += 1
        
        for num in arr2:
            while count[num] > 0:
                ans.append(num) 
                count[num] -= 1

        tmp = []
        for i in arr1:
            if i not in arr2:
                tmp.append(i)
        tmp.sort()
        return ans + tmp     