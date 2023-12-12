class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        arr = {key: idx for idx, key in enumerate(nums)}
        print(arr)
        for val, replace in operations:
            idx = arr[val]
            del arr[val]
            nums[idx] = replace
            arr[replace] = idx
        return nums
    
            