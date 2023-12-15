class OrderedStream:

    def __init__(self, n: int):
        self.string = [0] * n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.string[idKey - 1] = value
        
        res = []
        while self.ptr < len(self.string) and self.string[self.ptr] != 0:
            res.append(self.string[self.ptr])
            self.ptr += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)