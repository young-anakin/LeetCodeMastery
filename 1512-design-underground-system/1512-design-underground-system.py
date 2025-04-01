class UndergroundSystem:

    def __init__(self):
        self.Incoming = defaultdict(int)
        self.counter = defaultdict(int)
        self.avg = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.Incoming[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.avg[(self.Incoming[id][0], stationName)] = self.avg[(self.Incoming[id][0], stationName)] + (t - self.Incoming[id][1]) 
        self.counter[(self.Incoming[id][0], stationName)] +=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[(startStation, endStation)] / (self.counter[((startStation, endStation))])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)