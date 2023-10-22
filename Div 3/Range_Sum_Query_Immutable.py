class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.prefix_sum[left]
        rightsum = self.prefix_sum[right + 1]
        return rightsum - leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)