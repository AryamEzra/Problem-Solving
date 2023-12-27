class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
       #time: O(n logn) - beacuse of the sorting
        #space: O(n)

        arr = [(height, name) for name, height in zip(names, heights)]

        sorted_arr = sorted(arr, reverse = True)
        sort_names = [height for _, height in sorted_arr]

        return sort_names


        

        
        