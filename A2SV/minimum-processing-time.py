class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        #to decrease the maximum waiting time we give the maximum time tot he least processor
        #time: O(n*2)
        #space: O(n)

        tot = -1
        task = sorted(tasks, reverse = True)
        processorTime.sort()
        
        step = len(task)  // 4
        for i in range(step):
            for j in range(i*4, ((i+1)*4)):
                x = processorTime[i] + task[j]
                tot = max(x, tot)

        return tot


