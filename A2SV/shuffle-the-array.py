class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums) // 2
        res1 = nums[:n]
        res2= nums[n:]
        arr = []
        for i in range(n):
            arr.append(res1[i])
            arr.append(res2[i])
        return arr

        