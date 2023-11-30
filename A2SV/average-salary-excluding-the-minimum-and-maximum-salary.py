class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        avg = 0
        for i in range(1,len(salary)-1):
            avg += salary[i]
        return avg/(len(salary) - 2)
        