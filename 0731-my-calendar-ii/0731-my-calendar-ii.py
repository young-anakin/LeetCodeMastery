class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        # print(startTime, endTime)
        fl = True
        for i, j in self.double:
            if ((startTime <= i and startTime <= j) and (endTime <= i and endTime <= j)) or ((startTime >= i and startTime >= j) and (endTime >= i and endTime >= j)):
                fl = True
                # break
            else:
                fl = False
                break

        if not fl:
            return False

        for i, j in self.single:
            if ((startTime <= i and startTime <= j) and (endTime <= i and endTime <= j)) or ((startTime >= i and startTime >= j) and (endTime >= i and endTime >= j)):
                # fl = True
                continue
            else:
                # fl = False
                self.double.append([max(i, startTime), min(j, endTime)])
        
        self.single.append([startTime, endTime])
        # print("Single, ", self.single)
        # print("Double", self.double)
        

        
        return fl
        




# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)