class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #time: O(m+n)
        #space: o(m+n)

        f1 = len(firstList)
        s2 = len(secondList)
        
        l1 = 0
        l2 = 0
        ans = []
        while l1 < f1 and l2 < s2:
            inter = [max(firstList[l1][0], secondList[l2][0]), min(firstList[l1][1], secondList[l2][1])]
            if inter[0] <= inter[1]:
                ans.append(inter)
            if firstList[l1][1] < secondList[l2][1]:
                l1 += 1
            else:
                l2 += 1
        return ans



        