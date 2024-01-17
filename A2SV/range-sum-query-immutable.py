class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix_sum.append(cur)
        print(self.prefix_sum)
        
        

    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.prefix_sum[left-1] if left > 0 else 0
        rightsum = self.prefix_sum[right]
        return rightsum - leftsum
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)