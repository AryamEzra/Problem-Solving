class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        after = []
        equal = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                before.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            else:
                after.append(nums[i])
        return before + equal + after



        