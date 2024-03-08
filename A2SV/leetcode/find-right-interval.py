class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = []
        t = len(intervals)
        dic = {}
        store = []
        for idx,num in enumerate(intervals):
            dic[num[0]] = idx
            store.append([num[0], idx])
        store.sort()
        
        vals = []
        idxs = []
        for i in range(t):
            vals.append(store[i][0])
            idxs.append(store[i][1])

        for i in range(t):
            x = bisect_left(vals, intervals[i][1])
            if x == t:
                ans.append(-1)
            else:
                ans.append(dic[vals[x]])
        return ans