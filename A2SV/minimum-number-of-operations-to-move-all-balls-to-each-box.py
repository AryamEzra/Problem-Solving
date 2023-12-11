class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for index in range(len(boxes)):
            total = 0

            for left in range(index, -1, -1):
                if boxes[left] == "1":
                    total += index - left
            
            for right in range(index + 1, len(boxes)):
                if boxes[right] == "1":
                    total += right - index
   
            res.append(total) 
        return res