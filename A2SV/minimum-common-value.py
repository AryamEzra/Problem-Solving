class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        ptr1 = 0
        ptr2 = 0
        n1 = len(nums1)
        n2 = len(nums2)
        ans = 10 ** 9 + 1
        while ptr1 < n1 and ptr2 < n2:
            if nums1[ptr1] == nums2[ptr2]:
                ans = min(ans, nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return ans if ans != 10**9 + 1 else -1

        