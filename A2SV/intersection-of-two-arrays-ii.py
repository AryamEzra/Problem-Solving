class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #time: O(n)
        #space: O(n)
        
        ans = []
        count_num1 = Counter(nums1)
        count_num2 = Counter(nums2)

        for k,v in count_num1.items():
            if k in count_num2:
                ans.extend([k] * min(v, count_num2[k]))
        return ans


                


                
        
        