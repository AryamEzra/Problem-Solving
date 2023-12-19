
from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkin = {}
        self.time = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(stationName, t)

        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, intial_time = self.checkin[id]
        self.time[start_station][stationName].append(t - intial_time)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t = self.time[startStation][endStation]
        print(t)
        avg = sum(t) / len(t)
        return avg

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)