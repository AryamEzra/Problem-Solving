class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k):
            start = 0
            while start < k:
                arr[start], arr[k] = arr[k], arr[start]
                start += 1
                k -= 1
                
        n = len(arr)
        result = []

        for i in range(n-1, -1, -1):
            max_no = i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_no]: max_no = j
            if max_no != i:
                flip(max_no)
                flip(i)
                result.append(max_no+1)
                result.append(i+1)
        return result