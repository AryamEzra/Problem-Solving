class FrequencyTracker:

    def __init__(self):
        self.occur = defaultdict(int)
        self.num = defaultdict(int)
        
    def add(self, number: int) -> None:
        self.occur[number] += 1
        ans = self.occur[number]
        self.num[ans] += 1
        self.num[ans-1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.occur[number] > 0:
            self.occur[number] -= 1
            ans = self.occur[number]
            self.num[ans] += 1
            self.num[ans+1] -= 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.num[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)