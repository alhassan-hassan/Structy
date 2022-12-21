import collections
class UndergroundSystem:

    def __init__(self):
        self.checkIns = collections.defaultdict(list)
        self.checkOuts = collections.defaultdict(lambda : [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.checkIns.pop(id)
        key = (station,stationName)
        update = t - time

        self.checkOuts[key][0] += update
        self.checkOuts[key][1] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation,endStation)
        journeys, trips = self.checkOuts[key]
        
        return journeys / trips
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)