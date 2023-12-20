class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.count_one = 0
        self.unflipped_arr = [0] * size
        self.flipped_arr = [1] * size

    def fix(self, idx: int) -> None:
        if self.unflipped_arr[idx] == 0:
            self.unflipped_arr[idx] = 1
            self.flipped_arr[idx] = 0
            self.count_one += 1

    def unfix(self, idx: int) -> None:
        if self.unflipped_arr[idx] == 1:
            self.unflipped_arr[idx] = 0
            self.flipped_arr[idx] = 1
            self.count_one -= 1
        

    def flip(self) -> None:
        self.unflipped_arr, self.flipped_arr = self.flipped_arr, self.unflipped_arr
        self.count_one = self.size - self.count_one
        # so this makes it count of zeros

    def all(self) -> bool:
        if self.count_one == self.size:
            return True
        return False

    def one(self) -> bool:
        if self.count_one > 0:
            return True
        return False
        
    def count(self) -> int:
        return self.count_one 

    def toString(self) -> str:
        return "".join(str(i) for i in self.unflipped_arr)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()