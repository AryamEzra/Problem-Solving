class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #time: O(n)
        #space: O(1)

        if len(arr) < 3:
            return False
        elif arr == sorted(arr, reverse=True):
            return False
        elif arr == sorted(arr):
            return False
        else:
            left = 0
            right = len(arr) - 1
            max_num = max(arr)

            while left < right:
                if arr[left] < max_num and max_num > arr[right] and arr[left] < arr[left+1] and arr[right-1] > arr[right]:
                    left += 1
                    right -= 1
                elif arr[left] == max_num and arr[left] > arr[right] and arr[right-1] > arr[right]:
                    right -= 1
                elif arr[right] == max_num and arr[right] > arr[left] and arr[left] < arr[left+1]:
                    left += 1

                else:
                    return False
            return True
            
            
        
        