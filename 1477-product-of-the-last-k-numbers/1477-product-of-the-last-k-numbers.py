class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.prefix = [1]
        self.lastZero = -1
        self.curr = 0

    def add(self, num: int) -> None:
        self.curr +=1
        self.arr.append(num)
        if self.prefix[-1] == 0:
            self.lastZero = self.curr - 1
            self.prefix.append(num)
        else:
            self.prefix.append(self.prefix[-1] * num)
        

        

    def getProduct(self, k: int) -> int:
        # print(self.prefix, k, self.lastZero)

        # print(self.prefix[-1], self.prefix[- (k + 1)])
        if self.curr - k < self.lastZero:
            return 0
        if self.prefix[-(k+1)] == 0:
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[- (k+1)]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)