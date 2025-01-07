class CustomStack:

    def __init__(self, maxSize: int):
        self.mx = maxSize
        self.arr = []
        self.cp = 0
    def push(self, x: int) -> None:
        if self.cp < self.mx:
            self.arr.append(x)
            self.cp +=1

    def pop(self) -> int:
        if self.arr:
            x = self.arr.pop()
            self.cp -=1
            return x
        return -1
    def increment(self, k: int, val: int) -> None:
        for ind in range(min(k, self.cp)):
            self.arr[ind] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)