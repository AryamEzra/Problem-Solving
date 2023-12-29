class Solution:
    def smallestNumber(self, num: int) -> int:
        #time: O(nlogn)
        #space: O(n)

        if num == 0:
            return num

        elif num > 0:
            num_str = str(num)
            arr = []
            for i in range(len(num_str)):
                arr.append(int(num_str[i]))
            
            arr.sort()
            for i in range(len(arr)):
                if arr[i] == 0:
                    continue
                else:
                    x = i
                    break
            arr[0], arr[x] = arr[x], arr[0]
                
           
            x = "".join(str(i) for i in arr)
            x = int(x)
            return x

        else:
            num_str = str(num)
            arr = []
            for i in range(1, len(num_str)):
                arr.append(int(num_str[i]))
            arr = sorted(arr, reverse = True)
            
            x = "".join(str(i) for i in arr)
            x = int(x)
            x = x * -1
            return x 
            
            
        