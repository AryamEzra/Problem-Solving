class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        #time: O(n**2)
        #space: O(n)

        end = len(arr)
        ans = []
        for i in range(end):
            max_idx = arr.index(end) + 1
            if 1 < max_idx and max_idx < end:
                part = arr[:max_idx]
                part = part[::-1]
                arr[:max_idx] = part
                ans.append(max_idx)
                
                part2 = arr[:end]
                part2 = part2[::-1]
                arr[:end] = part2
                ans.append(end)

                
            elif max_idx == 1:
                part2 = arr[:end]
                part2 = part2[::-1]
                arr[:end] = part2
                ans.append(end)
            end -= 1
        return ans


        
        