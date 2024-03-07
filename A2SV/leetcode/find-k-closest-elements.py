class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        idx = bisect_left(arr, x)
        if idx == 0:
            return arr[:k]
        if idx == len(arr):
            return arr[-k:]
        l = idx - 1
        r = idx
        while (l >= 0 or r < len(arr)) and k > 0:
            if l < 0:
                ans.append(arr[r])
                r += 1
            elif r > len(arr) - 1:
                ans.append(arr[l])
                l -= 1
            else:
                left = abs(x - arr[l])
                right = abs(x - arr[r])
                if left <= right:
                    ans.append(arr[l])
                    l -= 1 
                else:
                    ans.append(arr[r])
                    r += 1

            k -= 1
        
        return sorted(ans)
                