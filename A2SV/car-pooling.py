class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #time: O(n)
        #space: O(n)

        car = [0] * 1001
        flag = True
        for pas, start, end in trips:
            car[start] += pas
            car[end] -= pas
        for i in range(1, len(car)):
            car[i] += car[i-1]
        for i in range(len(car)):
            if car[i] <= capacity:
                flag = True
            else:
                flag = False
                break
        print(car) 
        if flag == True:
            return True
        else:
            return False
            

        