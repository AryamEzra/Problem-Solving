from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        radiant = deque()
        s = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
    
        t = max(len(dire), len(radiant))       
        while dire and radiant:
            r = radiant.popleft()
            d = dire.popleft()
            if r > d:
                dire.append(d + s)
            else:
                radiant.append(r + s)
        if dire:
            return "Dire"
        else:
            return "Radiant"