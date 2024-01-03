class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = "_"
        undsc = 0
        ptr = 0
        while ptr < n:
            if nums[ptr] != "_":
                nums[ptr], nums[undsc] = nums[undsc], nums[ptr]
                undsc += 1
            ptr += 1
        k = 0
        for i in range(n):
            if nums[k] != "_":
                k += 1
            else:
                break
        return k
        