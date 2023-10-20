class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        #the length of nums1
        
        #merge in reverse order meaning we have t start filling the boxes fromt he right end by comparing the values of the last filled boxed in each array
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
    
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        # if nums 1 has a greater number in the first box that nums1 by the end then the reamaing nums2 will be added into the beginning of nums1 once we establish that all remaining elements of num 2 are less than the first element of nums1    
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1