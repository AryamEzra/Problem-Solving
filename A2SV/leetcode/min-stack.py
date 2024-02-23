class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        elif self.min and self.min[-1] >= val:
            self.min.append(val)

    def pop(self) -> None:
        if self.min  and self.stack[-1] == self.min[-1]:
            self.min.pop() 
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0  
    
    def getMin(self) -> int: 
        if self.min:
            return self.min[-1]
        else:
            return 0
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()