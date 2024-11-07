class UndergroundSystem:

    def __init__(self):
        self.checkIns = {}
        # self.travelTimes = collections.defaultdict(lambda: [0,0])
        self.travelTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkIns[id]
        trip = (startStation, stationName)
        tripDuration = t - startTime

        if trip in self.travelTimes:
            totalTime, count = self.travelTimes[trip]
            self.travelTimes[trip] = (totalTime + tripDuration, count + 1)
        else:
            self.travelTimes[trip] = (tripDuration,1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = (startStation, endStation)
        time, count = self.travelTimes[trip]
        return time / count


# class UndergroundSystem:

#     def __init__(self):
#         # Tracks the customer's check-in data (ID -> (station, time))
#         self.check_ins = {}
        
#         # Tracks travel time data between stations ((start, end) -> (total_time, trip_count))
#         self.travel_times = {}

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         # Register a customer's check-in info
#         self.check_ins[id] = (stationName, t)

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         # Retrieve check-in info for the customer
#         start_station, start_time = self.check_ins[id]
        
#         # Calculate travel time
#         travel_time = t - start_time
        
#         # Record or update the travel data
#         route = (start_station, stationName)
        
#         if route in self.travel_times:
#             total_time, trip_count = self.travel_times[route]
#             self.travel_times[route] = (total_time + travel_time, trip_count + 1)
#         else:
#             self.travel_times[route] = (travel_time, 1)

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         # Fetch total time and trip count for the requested route
#         total_time, trip_count = self.travel_times[(startStation, endStation)]
        
#         # Calculate and return the average
#         return total_time / trip_count
# # class UndergroundSystem:

# #     def __init__(self):
# #         self.checksData = {}
# #         self.travelData = collections.defaultdict(lambda: [0, 0])
        
# #     def checkIn(self, id: int, stationName: str, t: int) -> None:
# #         self.checksData[id]=[stationName,t]
        
# #     def checkOut(self, id: int, stationName: str, t: int) -> None:
# #         prevStationName,startT = self.checksData[id]
# #         # USED WHEN THE LAMBDA FUNCTION IS NOT USED
# #         # totalTime, count = 0,0
# #         # if self.travelData[(prevStationName,stationName)] :
# #         #     totalTime, count = self.travelData[(prevStationName,stationName)] 
# #         self.travelData[(prevStationName,stationName)][0] += t - startT
# #         self.travelData[(prevStationName,stationName)][1] += 1

# #     def getAverageTime(self, startStation: str, endStation: str) -> float:
# #         totalTime, count = self.travelData[(startStation,endStation)]
# #         return totalTime/count
        


# # # Your UndergroundSystem object will be instantiated and called as such:
# # # obj = UndergroundSystem()
# # # obj.checkIn(id,stationName,t)
# # # obj.checkOut(id,stationName,t)
# # # param_3 = obj.getAverageTime(startStation,endStation)


# # """
# # QUESTIONS TO ASK:
# # 1.  Error Handling:
# #     How should we handle cases where getAverageTime is called for a start and end station combination that has never 
# #     been traveled before?

# # 2.  Handling Invalid or Inconsistent Events:
# #     Do we need to handle cases where a customer checks out without first checking in, or vice versa?
# #     Should we assume that all events (check-in and check-out) will be consistent and ordered chronologically?

# # Complexity Analysis

# #     Time complexity : O(1)O(1)O(1) for all.


# #     Space complexity : O(P+S^2), where SSS is the number of stations on the network, and PPP is the number of 
# #     passengers making a journey concurrently during peak time.

# #     The program uses two HashMaps. We need to determine the maximum sizes these could become.

# #     Firstly, we'll consider checkInData. This HashMap holds one entry for each passenger who has checkIn(...)ed, but 
# #     not checkOut(...)ed. Therefore, the maximum size this HashMap could be is the maximum possible number of passengers
# #     making a journey at the same time, which we defined to be PPP. Therefore, the size of this HashMap is O(P)O(P)O(P).

# #     Secondly, we need to consider journeyData. This HashMap has one entry for each pair of stations that has had at 
# #     least one passenger start and end a journey at those stations. Over time, we could reasonably expect every possible 
# #     pair of the SSS stations on the network to have an entry in this HashMap, which would be O(S^2)
# #  ).
# # """

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# 
# import collections
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
    

class UndergroundSystem:

    def __init__(self):
        self.checkIns = {} # id -> (station, time)
        self.tracker = {} # (start, end) -> [total, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station, time = self.checkIns[id]
        
        if (station, stationName) not in self.tracker:
            self.tracker[(station, stationName)] = [0, 0]
        self.tracker[(station, stationName)][0] += t - time
        self.tracker[(station, stationName)][1] += 1
       
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.tracker[(startStation, endStation)]
        return time / count

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)