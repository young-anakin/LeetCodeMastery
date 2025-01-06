class MyCalendar:

    def __init__(self):
        self.arr = []

    def book(self, startTime: int, endTime: int) -> bool:
        # x = bisect.bisect_left(arr, startTime)

        if len(self.arr) == 0:
            self.arr.append((startTime, endTime))
            return True
        else:
            fl = False
            for i, j in self.arr:
                if ((startTime <= i and startTime <= j) and (endTime <= i and endTime <= j))  or ((startTime >= i and startTime >= j) and (endTime >=i and endTime >= j) ):
                    fl = True
                else:
                    fl = False
                    break
            if fl:
                self.arr.append((startTime, endTime))
        # print(self.arr)
        return fl

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)