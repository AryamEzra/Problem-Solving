class ATM:

    def __init__(self):
        self.money = [20, 50, 100, 200, 500]
        self.cash = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.cash[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        give = [0 for I in range(5)]
        for i in range(4, -1, -1):
            # i is the given value index
            possible_give = amount // self.money[i]
            give[i] = min(possible_give, self.cash[i])
            amount -= give[i] * self.money[i]

        if amount == 0:
            for i in range(5):
                self.cash[i] -= give[i]
            return give
        else:
            return [-1]
         
            

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)